from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.views.decorators.http import require_POST
from .models import User
from .forms import SignUpForm, CustomUserChangeForm

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:main')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'posts:main')
            
    return render(request, 'users/login.html')


def logout(request):
    auth_logout(request)
    return redirect('users:login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  
            form.save()  
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('users:login')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }    
    
    return render(request, 'users/signup.html', context)


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            print(3)
            return redirect('posts:main')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/update.html', context)