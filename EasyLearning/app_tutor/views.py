from django.shortcuts import render, get_object_or_404
from EasyLearning.decorators import tutor_required
from django.contrib.auth.decorators import login_required

from app_quiz.models import Question, Quiz, Answer, TakenQuiz

# Create your views here.


@login_required
@tutor_required
def tutorProfile(request):
    return render(request, 'app_tutor/tutor_profile.html', {})


@login_required
@tutor_required
def ResultView(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    results = TakenQuiz.objects.filter(quiz=quiz)

    return render(request, 'app_tutor/view_result.html', {'results': results})
