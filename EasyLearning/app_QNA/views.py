from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AskedQuestion, Reply
from app_course.models import Catagory
from .forms import askQuestionForm, replyForm
from django.contrib import messages
# Create your views here.


@login_required
def questionList(request):
    questions = AskedQuestion.objects.all()
    catagories = Catagory.objects.all()
    return render(request, 'QNA_home.html', {'questions': questions, 'catagories': catagories})


@login_required
def quesWithCatagory(request, catg_pk):
    catagory = get_object_or_404(Catagory, pk=catg_pk)
    catagories = Catagory.objects.all()
    questions = AskedQuestion.objects.filter(catagory=catagory)
    return render(request, 'QNA_home.html', {'questions': questions, 'catagories': catagories})


@login_required
def askQuestion(request):
    if request.method == 'POST':
        form = askQuestionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, 'Question Posted Successfully....')
            return redirect('app_QNA:asked_list')
    else:
        form = askQuestionForm()
    return render(request, 'app_QNA/question_add.html', {'form': form})


@login_required
def questionDetails(request, ques_pk):
    question = AskedQuestion.objects.get(pk=ques_pk)

    if request.method == 'POST':
        form = replyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.question = question
            obj.save()
            messages.success(request, 'Answer Posted Successfully....')
            form = replyForm()
    else:
        form = replyForm()

    replies = Reply.objects.filter(question=question)
    num_of_ans = replies.count()

    return render(request, 'app_QNA/question_details.html', {
        'form': form,
        'num_of_ans': num_of_ans,
        'question': question,
        'replies': replies,
    })


@login_required
def deleteQuestion(request, ques_pk):
    question = get_object_or_404(AskedQuestion, pk=ques_pk)
    if request.user == question.author:
        question.delete()
        messages.warning(request, 'Question Deleted Successfully...')
    else:
        messages.error(request, 'You are not allowed to delete this question')
    return redirect('app_QNA:asked_list')
