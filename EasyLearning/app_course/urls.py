from django.urls import path
from . import views

app_name = 'app_course'

urlpatterns = [
    path('add_course/', views.addCourse, name="add_course"),
    path('add_article/<pk>/', views.addArticle, name="add_article"),
    path('course_details/<pk>/', views.courseDetails, name="course_details"),
    path('delete_course/<pk>/', views.deleteCourse, name="delete_course"),
    path('article_details/<pk>/', views.articleDetails, name="article_details"),
    path('edit_article/<pk>/', views.editArticle, name="edit_article"),
    path('delete_article/<pk>/', views.deleteArticle, name="delete_article"),
]
