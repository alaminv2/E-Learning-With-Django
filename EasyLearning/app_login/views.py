from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView
from .forms import signUpForm, loginForm
from django.contrib.auth.forms import AuthenticationForm
from app_login.models import User
from app_quiz.models import Student
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

# Create your views here.


def chooseAccount(request):
    return render(request, 'app_login/choose_account.html')


def studentSignUp(request):
    form = signUpForm()
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                obj = form.save(commit=False)
                obj.is_student = True
                obj.save()
                Student.objects.create(user=obj)
                messages.success(
                    request, 'Student Account Created Successfully')
                return redirect('app_login:login')
    return render(request, 'app_login/student_signup.html', {'form': form})


def tutorSignUp(request):
    form = signUpForm()
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.is_tutor = True
            obj.save()
            messages.success(request, 'Tutor Account Created Successfully')
            return redirect('app_login:login')

    return render(request, 'app_login/tutor_signup.html', {'form': form})


def loginView(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_student:
                    messages.success(
                        request, 'Logged in as Student Successfully')
                    return redirect('home')
                if user.is_tutor:
                    messages.success(
                        request, 'Logged in as Tutor Successfully')
                    return redirect('app_tutor:tutor_profile')

    return render(request, 'app_login/login.html', {'form': form})


@login_required
def logoutView(request):
    logout(request)
    messages.warning(request, 'Logged out Successfully')
    return redirect('app_login:login')
