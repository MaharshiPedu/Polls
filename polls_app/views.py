from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.
def index(request):
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_questions_list])
    context = {'latest_questions_list': latest_questions_list}
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    print("123")
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    return HttpResponse(f"You're voting for question {question_id}")

