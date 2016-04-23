from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from operator import itemgetter
from polls.models import *


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 10)
    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return  objects_page, paginator

def id_question(request, id):
    realid=int(id)
    question = Question.manager.by_id(realid)
    answers_list = Answer.manager.by_id(realid)
    page_answers, paginator = paginate(answers_list, request)
    return render(request, 'answers.html',{'question':question, 'answers': page_answers})


def new_questions(request):
    question_list = Question.manager.new()
    page_questions, paginator = paginate(question_list, request)
    return render(request, 'questions.html', {'questions': page_questions,
                                              'title': 'New questions',
                                              })

def hot_questions(request):
    question_list = Question.manager.hot()
    page_questions, paginator = paginate(question_list, request)
    return render(request, 'questions.html', {'questions': page_questions,
                                              'title': 'Hot questions',
                                              })

def tags_question(request, tag):
    question_list = Question.manager.by_tags(tag)
    page_questions, paginator = paginate(question_list, request)
    return render(request, 'questions.html', {'questions': page_questions,
                                              'title': 'Questions with tag: ' + tag,
                                              })









def signup(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def ask(request):
    return render(request, 'ask.html')