from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'This email address is already registered with our system.')
                    return redirect('register')

                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # login after registration
                    #auth.login(request, user)
                    #messages.success(request, 'User has been registered and is now logged in. ')
                    # redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can now login.')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match.')
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
