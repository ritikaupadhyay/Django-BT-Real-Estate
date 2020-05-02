from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Register user
        messages.error(request, 'Testing error messages')
        return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        # Register user
        pass

    else:
        return redirect('index')


def dashboard(request):
    if request.method == 'POST':
        # Register user
        pass

    else:
        return render(request, 'accounts/dashboard.html')
