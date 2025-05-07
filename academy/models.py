from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(help_text="Order in which lessons appear")

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    pass_mark = models.IntegerField(default=80)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()

    def __str__(self):
        return f"Cert for {self.user.username} (Score: {self.score}%)"