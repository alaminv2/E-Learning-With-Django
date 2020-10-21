from django.contrib import admin
from .models import Course, Catagory, Article

# Register your models here.

admin.site.register(Catagory)
admin.site.register(Article)
admin.site.register(Course)
