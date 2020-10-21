from django.db import models
from app_login.models import User
from app_course.models import Catagory
# Create your models here.


class AskedQuestion(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ask_ques')
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, related_name='catg')
    title = models.CharField(max_length=264)
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + '. ' + self.title

    class Meta:
        ordering = ('-created',)


class Reply(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rep_auth')
    question = models.ForeignKey(
        AskedQuestion, on_delete=models.CASCADE, related_name='ques')
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) > 50:
            return str(self.pk) + '. ' + self.text[0:50] + '........'
        else:
            return str(self.pk) + '. ' + self.text

    class Meta:
        ordering = ('-created',)
