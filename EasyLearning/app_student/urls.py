from django.urls import path
from . import views

app_name = 'app_student'

urlpatterns = [
    path('selected/<pk>/', views.selectedCourse, name="selected"),
    path('read/<pk>/', views.readView, name="read"),
    path('take_quiz/<int:quiz_pk>/', views.takeQuizView, name='take_quiz'),
    path('taken_quizzes/', views.takenQuizList, name="taken_quizzes"),
    path('retake/<int:taken_pk>/', views.retakeQuiz, name="retake"),
]
