from django.shortcuts import render,redirect
from .models import Target
from django.contrib.auth.decorators import login_required

    
def index(request):
    if 'n' in request.GET and 'l' in request.GET:
        first_name = str(request.GET['n']).lower()
        last_name = str(request.GET['l']).lower()
        if Target.objects.filter(first_name=first_name,last_name=last_name).exists():
            target = Target.objects.filter(first_name=first_name,last_name=last_name).first()
            target.count=target.count+1
            target.save()
            # print("Sayaç arttı")
        else:
            Target.objects.create(first_name=first_name, last_name=last_name)
            # print("Yeni Kayıt Oluşturuldu")

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