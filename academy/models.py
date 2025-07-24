# academy/models.py

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Lesson(models.Model):
    title   = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    order   = models.PositiveIntegerField(default=0)
    content = RichTextUploadingField()

    def __str__(self):
        return f"{self.order}. {self.title}"

class LessonSection(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        related_name="sections",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, blank=True)
    body  = RichTextUploadingField(blank=True)
    image = models.ImageField(
        upload_to="lesson_images/",
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.lesson.title} – Section {self.order}"

class Quiz(models.Model):
    lesson    = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    pass_mark = models.IntegerField(default=80)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    question   = models.ForeignKey(Question, on_delete=models.CASCADE)
    text       = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'✓' if self.is_correct else '✗'})"

class Certificate(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson    = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    score     = models.FloatField()

    def __str__(self):
        return f"Cert for {self.user.username} – {self.lesson.title} ({self.score}%)"

class LessonProgress(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson       = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed    = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "lesson")

    def __str__(self):
        status = "Done" if self.completed else "In progress"
        return f"{self.user.username} – {self.lesson.title}: {status}"

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SectionProgress(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    section   = models.ForeignKey(LessonSection, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "section")

    def __str__(self):
        return f"{self.user.username} viewed {self.section}"
