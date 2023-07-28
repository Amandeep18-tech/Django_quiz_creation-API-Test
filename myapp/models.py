from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    quiz_score_user = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Exam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name
    
class Question(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name

class LoginLog(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100)
    login_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_at}"


