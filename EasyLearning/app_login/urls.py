from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('choose/', views.chooseAccount, name="choose"),
    path('signup_1/', views.studentSignUp, name="student_signup"),
    path('signup_2/', views.tutorSignUp, name="tutor_signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
]
