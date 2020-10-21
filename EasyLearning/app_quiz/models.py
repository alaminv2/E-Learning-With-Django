from django.db import models
from app_login.models import User
from app_course.models import Catagory

# Create your models here.


class Quiz(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='quiz_author')
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, related_name='quiz_catagory', null=True)
    title = models.CharField(max_length=264)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + ". " + self.title

    class Meta:
        ordering = ('-created',)


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=264)

    def __str__(self):
        return str(self.pk) + ". " + self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    text = models.CharField(max_length=264)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="students")
    quizzes = models.ManyToManyField(Quiz, through="TakenQuiz")

    def get_unanswered_questions(self, quiz):
        answered_pk = self.student_answers.filter(
            answer__question__quiz=quiz).values_list('answer__question__pk', flat=True)
        unanswered = quiz.questions.exclude(
            pk__in=answered_pk).order_by('title')
        return unanswered

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="quiz_taker")
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="taken_quiz")
    score = models.FloatField()
    passed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + ". " + self.quiz.title

    class Meta:
        ordering = ('-created',)


class StudentAnswer(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student_answers", null=True)
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name="submitted")

    def __str__(self):
        return str(self.pk) + ". " + self.answer.text
