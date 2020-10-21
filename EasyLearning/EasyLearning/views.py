from django.shortcuts import render
from app_course.models import Course, Catagory, Article


def homeView(request):
    courses = Course.objects.all()
    catagories = Catagory.objects.all()
    return render(request, 'course_home.html', {'courses': courses, 'catagories': catagories})


def courseWithCatagory(request, pk):
    catagory = Catagory.objects.get(pk=pk)
    courses = Course.objects.filter(catagory=catagory)
    catagories = Catagory.objects.all()

    return render(request, 'course_home.html', {'courses': courses, 'catagories': catagories})


def featureTree(request):
    return render(request, 'Feature_tree.html')
