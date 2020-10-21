from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.db import transaction

from django.contrib.auth.decorators import login_required
from EasyLearning.decorators import tutor_required
from django.contrib import messages

# Froms And Models
from .forms import addQuizForm, addQuestionForm, BaseAnswerInlineFormSet
from django.forms import inlineformset_factory
from django import forms
from .models import Quiz, Question, Answer, StudentAnswer, Student, TakenQuiz
from app_course.models import Catagory

# Create your views here.


@login_required
def quizHomeView(request):
    quizzes = Quiz.objects.all()
    catagories = Catagory.objects.all()
    return render(request, 'quiz_home.html', {'quizzes': quizzes, 'catagories': catagories})


@login_required
def quizWithCatagory(request, catg_pk):
    catagory = get_object_or_404(Catagory, pk=catg_pk)
    quizzes = Quiz.objects.filter(catagory=catagory)
    catagories = Catagory.objects.all()

    return render(request, 'quiz_home.html', {'quizzes': quizzes, 'catagories': catagories})


@login_required
@tutor_required
def addQuizView(request):
    if request.method == 'POST':
        form = addQuizForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, 'Quiz Added Successfully....')
            return redirect('app_quiz:quiz_details', obj.pk)
    else:
        form = addQuizForm()
    return render(request, 'app_quiz/tutor/add_edit_quiz.html', {'form': form, 'created': False})


@login_required
@tutor_required
def quizDetailsView(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    question_list = Question.objects.filter(quiz=quiz)
    return render(request, 'app_quiz/tutor/quiz_details.html', {
        'question_list': question_list,
        'quiz': quiz,
        'quiz_pk': quiz_pk,
    })


@login_required
@tutor_required
def editQuizView(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    form = addQuizForm(instance=quiz)
    if request.method == 'POST':
        form = addQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quiz Saved Successfully....')
            return redirect('app_quiz:quiz_details', quiz_pk)
    return render(request, 'app_quiz/tutor/add_edit_quiz.html', {'form': form, 'created': True})


@login_required
@tutor_required
def deleteQuizView(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    quiz.delete()
    messages.warning(request, 'Quiz Deleted Successfully....')
    return redirect('app_tutor:tutor_profile')


@login_required
@tutor_required
def addQuestionView(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    if request.method == 'POST':
        form = addQuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.quiz = quiz
            obj.save()
            messages.success(request, 'Question Added Successfully....')
            return redirect('app_quiz:add_options', quiz_pk, obj.pk)
    else:
        form = addQuestionForm()
    return render(request, 'app_quiz/tutor/add_edit_question.html', {'form': form})


@login_required
@tutor_required
def deleteQuestion(request, ques_pk, quiz_pk):
    question = get_object_or_404(Question, pk=ques_pk)
    if question is not None:
        question.delete()
        messages.warning(request, 'Question Deleted Successfully....')
        return redirect('app_quiz:quiz_details', quiz_pk)


@login_required
@tutor_required
def addOptionsView(request, quiz_pk, ques_pk):
    curr_question = get_object_or_404(Question, pk=ques_pk)

    AnswerFormSet = inlineformset_factory(
        Question,
        Answer,
        formset=BaseAnswerInlineFormSet,
        fields=('text', 'is_correct'),
        extra=4,
        min_num=4,
        max_num=4,
        validate_min=True,
        validate_max=True
    )

    if request.method == 'POST':
        ques_form = addQuestionForm(request.POST, instance=curr_question)
        formset = AnswerFormSet(request.POST, instance=curr_question)
        if ques_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                ques_form.save()
                formset.save()
                messages.success(
                    request, 'Options Added to Question Successfully....')

            return redirect('app_quiz:quiz_details', quiz_pk)
    else:
        ques_form = addQuestionForm(instance=curr_question)
        formset = AnswerFormSet(instance=curr_question)

    return render(request, 'app_quiz/tutor/add_edit_options.html', {'formset': formset, 'ques_form': ques_form})
