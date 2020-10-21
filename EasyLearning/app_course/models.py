from django.db import models
from app_login.models import User

# Create your models here.


class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Catagories'


class Course(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="course_author")
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, related_name="course_catagory")
    name = models.CharField(max_length=264)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)


class Article(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_author")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="article_course")
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
