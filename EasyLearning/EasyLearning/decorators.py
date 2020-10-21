from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse


def tutor_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_tutor and not request.user.is_student:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))
    return wrap


def student_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_student and not request.user.is_tutor:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))
    return wrap
