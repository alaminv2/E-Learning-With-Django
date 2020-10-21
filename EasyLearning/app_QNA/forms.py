from django import forms
from .models import AskedQuestion, Reply
from app_course.models import Catagory


class askQuestionForm(forms.ModelForm):
    catagory = forms.ModelChoiceField(queryset=Catagory.objects.all())
    text = forms.CharField(label="", widget=forms.Textarea(attrs={
        'placeholder': 'Ask To Learn'
    }))

    class Meta:
        model = AskedQuestion
        fields = ('catagory', 'title', 'text')


class replyForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={
        'placeholder': 'Give Answer........',
    }))

    class Meta:
        model = Reply
        fields = ('text',)
