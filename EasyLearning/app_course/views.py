from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .forms import addCourseForm, addArticleForm
from .models import Catagory, Course, Article

from django.contrib.auth.decorators import login_required
from EasyLearning.decorators import tutor_required
from django.contrib import messages

# Create your views here.


@login_required
@tutor_required
def addCourse(request):
    form = addCourseForm()
    if request.method == 'POST':
        form = addCourseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, 'Courses Added Successfully....')
            return HttpResponseRedirect(reverse('app_course:course_details', kwargs=({'pk': obj.pk})))
    return render(request, 'app_course/add_course.html', {'form': form})


@login_required
@tutor_required
def addArticle(request, pk):
    cur_course = get_object_or_404(Course, pk=pk, author=request.user)
    course_form = addCourseForm(instance=cur_course)
    form = addArticleForm()
    if request.method == 'POST':
        form = addArticleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.course = cur_course
            obj.save()
            messages.success(request, 'Article Added Successfully....')
            return HttpResponseRedirect(reverse('app_course:course_details', kwargs=({'pk': pk})))
    return render(request, 'app_course/add_article.html', {'form': form, 'course_form': course_form})


@login_required
@tutor_required
def courseDetails(request, pk):
    cur_course = get_object_or_404(Course, pk=pk, author=request.user)
    return render(request, 'app_course/course_details.html', {'course': cur_course})


@login_required
@tutor_required
def deleteCourse(request, pk):
    obj = get_object_or_404(Course, pk=pk, author=request.user)
    obj.delete()
    messages.warning(request, 'Courses Deleted Successfully....')
    return redirect('app_tutor:tutor_profile')


@login_required
@tutor_required
def articleDetails(request, pk):
    cur_article = get_object_or_404(Article, pk=pk, author=request.user)
    return render(request, 'app_course/article_details.html', {'article': cur_article})


@login_required
@tutor_required
def editArticle(request, pk):
    cur_article = get_object_or_404(Article, pk=pk, author=request.user)
    form = addArticleForm(instance=cur_article)
    if request.method == 'POST':
        form = addArticleForm(request.POST, instance=cur_article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article Saved Successfully....')
            return HttpResponseRedirect(reverse('app_course:article_details', kwargs=({'pk': pk})))
    return render(request, 'app_course/edit_article.html', {'form': form})


@login_required
@tutor_required
def deleteArticle(request, pk):
    obj = get_object_or_404(Article, pk=pk, author=request.user)
    course_pk = obj.course.pk
    obj.delete()
    messages.warning(request, 'Article Deleted Successfully....')
    return HttpResponseRedirect(reverse('app_course:course_details', kwargs=({'pk': course_pk})))
