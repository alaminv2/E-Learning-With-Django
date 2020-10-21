from django import forms
from .models import Quiz, Question, Answer


class addQuizForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Quiz
        fields = ('title',)


class addQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title',)


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_correct') == True:
                count += 1

        if count != 1:
            raise forms.ValidationError(
                'There must be One and Only One correct answer...!')
