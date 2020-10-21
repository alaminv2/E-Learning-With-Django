from django.urls import path
from . import views

app_name = 'app_tutor'

urlpatterns = [
    path('', views.tutorProfile, name="tutor_profile"),
    path('result/<int:quiz_pk>/', views.ResultView, name="result"),
]
