from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from EasyLearning.decorators import student_required
from django.db import transaction
from django.contrib import messages

# Models And Forms
from app_course.models import Course, Catagory, Article
from app_quiz.models import Quiz, StudentAnswer, TakenQuiz
from .forms import takeQuizForm


@login_required
def selectedCourse(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'app_student/course_details.html', {'course': course})


@login_required
def readView(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'app_student/article_details.html', {'article': article})


@login_required
@student_required
def takeQuizView(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    student = request.user.students

    if student.quizzes.filter(pk=quiz_pk).exists():
        return redirect('app_student:taken_quizzes')

    num_of_question = quiz.questions.count()
    unanswered = student.get_unanswered_questions(quiz)
    num_of_unanswered = unanswered.count()
    question = unanswered.first()

    if request.method == 'POST':
        form = takeQuizForm(request.POST, instance=question)
        if form.is_valid():
            with transaction.atomic():
                obj = form.save(commit=False)
                obj.student = student
                obj.save()
                if student.get_unanswered_questions(quiz).exists():
                    return redirect('app_student:take_quiz', quiz_pk)
                else:
                    num_of_correct_ans = student.student_answers.filter(
                        answer__question__quiz=quiz, answer__is_correct=True).count()
                    score = round((num_of_correct_ans / num_of_question) * 100)
                    passed = False
                    if score >= 60:
                        passed = True
                    TakenQuiz.objects.create(
                        student=student, quiz=quiz, score=score, passed=passed)

                    messages.success(
                        request, 'Quiz Completed Successfully....See Your Profile')
                    return redirect('app_quiz:quiz_home')
    else:
        form = takeQuizForm(instance=question)

    return render(request, 'app_student/take_quiz.html', {
        'form': form,
        'question': question
    })


@login_required
@student_required
def takenQuizList(request):
    student = request.user.students
    taken_quiz_list = student.quiz_taker.all()
    print(taken_quiz_list)
    return render(request, 'app_student/student_profile.html', {
        'taken_quiz_list': taken_quiz_list,
    })


@login_required
@student_required
def retakeQuiz(request, taken_pk):
    taken_quiz = get_object_or_404(TakenQuiz, pk=taken_pk)
    quiz = taken_quiz.quiz
    taken_quiz.delete()
    answer_list = StudentAnswer.objects.filter(
        student=request.user.students, answer__question__quiz=quiz).all()
    answer_list.delete()
    return redirect('app_student:take_quiz', quiz.pk)
