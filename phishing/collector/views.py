from django.shortcuts import render,redirect
from .models import Target
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def olta(r):
    if 'n' in r.GET and 'l' in r.GET:
        first_name = str(r.GET['n']).lower()
        last_name = str(r.GET['l']).lower()
        print(first_name)
        print(last_name)
        if Target.objects.filter(user=r.user).exists():
            target = Target.objects.filter(user=r.user).first()
            target.count=target.count+1
            target.save()
        else:
            username = f"{first_name}.{last_name}@yildizskylab.com"
            password = f"{first_name}.{last_name}.change.me"
            user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name)
            user.save()
            target = Target.objects.create(user=user)
            target.save()
    return redirect('index')

@login_required
def index(request):
    targets = Target.objects.all()
    return render(request, 'index.html', {'targets': targets})

@login_required
def delete_record(r):
    if r.user.is_superuser:
        first_name = str(r.GET['n']).lower()
        last_name = str(r.GET['l']).lower()
        target = Target.objects.filter(first_name=first_name,last_name=last_name)
        target.delete()
        
        return redirect('index')
    else:
        return render(r,'login')