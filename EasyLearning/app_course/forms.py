from django import forms
from .models import Catagory, Course, Article


class addCourseForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Course Name'}))

    class Meta:
        model = Course
        fields = ('name', 'catagory')


class addArticleForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Article Title'}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'placeholder': 'What\'s on your mind....!!!!!!!!',
    }))

    class Meta:
        model = Article
        fields = ('title', 'content')
