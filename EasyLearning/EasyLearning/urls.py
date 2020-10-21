
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView, name="home"),
    path('course_of/<pk>/', views.courseWithCatagory, name="course_of"),
    path('features/', views.featureTree, name='features'),

    path('login/', include('app_login.urls')),
    path('tutor/', include('app_tutor.urls')),
    path('course/', include('app_course.urls')),
    path('student/', include('app_student.urls')),
    path('quiz/', include('app_quiz.urls')),
    path('QNA/', include('app_QNA.urls')),
]
