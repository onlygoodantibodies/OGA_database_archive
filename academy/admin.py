from django.contrib import admin
from .models import Lesson, Quiz, Question, Answer, Certificate

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4  # Shows 4 answer fields per question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Certificate)