from django import forms
from app_quiz.models import StudentAnswer, Answer


class takeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        label="",
        empty_label=None
    )

    class Meta:
        model = StudentAnswer
        fields = ('answer',)

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('instance')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = Answer.objects.filter(
            question=question)
