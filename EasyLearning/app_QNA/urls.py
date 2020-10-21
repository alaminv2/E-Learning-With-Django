from django.urls import path
from . import views

app_name = 'app_QNA'

urlpatterns = [
    path('asked/', views.questionList, name="asked_list"),
    path('question_of/<int:catg_pk>/', views.quesWithCatagory, name="ques_of"),
    path('ask/', views.askQuestion, name="ask"),
    path('question/<int:ques_pk>/', views.questionDetails, name="question_details"),
    path('delete_ques/<int:ques_pk>/', views.deleteQuestion, name="delete_ques"),
]
