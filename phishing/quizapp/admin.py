from django.contrib import admin
from .models import Quiz
# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ["question", "is_active"]
    list_filter = ["is_active"]

admin.site.register(Quiz,QuizAdmin)