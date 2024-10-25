from django.shortcuts import render,redirect
from .models import Quiz
from django.http import JsonResponse
import json
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def quiz(r):
    
    questions = Quiz.objects.filter(is_active=True)
    if r.method == "POST":
        total = 100
        answers = []
        for q in range(1,questions.count()+1):
            try:
                answer = r.POST[f"q{q}"]
                answers.append(answer)
            except MultiValueDictKeyError:
                break
        ppq = 100/len(questions)
        
        for i in range(0,questions.count()):
            if not (answers[i] == questions[i].true_opt):
                total-=ppq
                
        
        if total<50:
            print("Başarısız")
        else:
            print("Başarılı")
        print(answers)
        return redirect('index')
    else:
        return render(r,'quiz.html',{'questions':questions})