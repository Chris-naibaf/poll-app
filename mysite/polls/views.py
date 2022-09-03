# from django.shortcuts import render - Esto estaba aquí cuando llegué así
# que no lo eliminaré por el momento.
from django.http import HttpResponse
from .models import Question

# Create your views here.

# Esta es una de las formas más sencillas de crear una vista.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])

    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
