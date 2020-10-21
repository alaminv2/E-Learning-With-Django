from django.urls import path
from . import views


app_name = 'app_quiz'

urlpatterns = [
    path('', views.quizHomeView, name="quiz_home"),
    path('quiz_of/<int:catg_pk>/', views.quizWithCatagory, name="quiz_of"),

    path('add_quiz/', views.addQuizView, name="add_quiz"),
    path('edit_quiz/<int:quiz_pk>/', views.editQuizView, name="edit_quiz"),
    path('details/<int:quiz_pk>/', views.quizDetailsView, name="quiz_details"),
    path('delete_quiz/<int:quiz_pk>/', views.deleteQuizView, name="delete_quiz"),

    path('add_question/<int:quiz_pk>/',
         views.addQuestionView, name="add_question"),
    path('delete_question/<int:ques_pk>/<int:quiz_pk>/',
         views.deleteQuestion, name="delete_question"),

    path('add_options/<int:quiz_pk>/<int:ques_pk>/',
         views.addOptionsView, name="add_options"),
]
