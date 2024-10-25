from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated: return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Diğer alanlar ekleyin (örn. email)

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Hesabınız oluşturuldu!')
        return redirect('login')  # Giriş sayfasına yönlendirin
    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated: return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Ana sayfaya yönlendirin
        else:
            messages.error(request, 'Hatalı giriş!')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')  # Giriş sayfasına yönlendirin