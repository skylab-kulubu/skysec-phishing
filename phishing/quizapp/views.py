from django.shortcuts import render,redirect
from .models import Quiz
from django.http import JsonResponse
import json
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from collector.models import Target
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
            target = Target.objects.filter(user=r.user)
            target.is_completed=True
            target.save()
            message = "Testi Geçtin!"
        else:
            message = "Testi Tekrar Çözün!"
        print(answers)
        return redirect('index',{"message":message})
    else:
        try:
            target = Target.objects.filter(user=r.user)
            if not Target.objects.filter(user=r.user).first().is_completed:
                return render(r,'quiz.html',{'questions':questions})
            else:
                return redirect('index')
        except:
            return redirect('index')