from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def about(request):
    return render(request, 'about.html')


def user_signin(request):
    return render(request, 'user_signin.html')


def user_registration(request):
    return render(request, 'user_registration.html')
