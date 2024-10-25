from django.shortcuts import render
from .models import Quiz
# Create your views here.


def quiz(r):
    questions = Quiz.objects.filter(is_active=True)
    
    return render(r,'quiz.html',{'questions':questions})