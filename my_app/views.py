from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from operator import itemgetter
import random
questions = []
answers = []
question_tags = ['give', 'me', 'my', 'flowers', 'while', 'i', 'still', 'can', 'smell', 'them']

for i in range(100):
    questions.append(
        {'id': i,
         'title': 'Question #{}. Some text following question number'.format(i),
         'body': '''?????????????????????????????????????.''',
         'tags': [question_tags[random.randint(0, len(question_tags) - 1)],
                  question_tags[random.randint(0, len(question_tags) - 1)],
                  question_tags[random.randint(0, len(question_tags) - 1)]],
         'likes': random.randint(0, 1000),
         'Answers': random.randint(0, 10),
         }
    )

for i in range(10):
    answers.append(
        {'id': i,
         'body': '''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.''',
         'likes': random.randint(0, 1000),
         }
    )
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
    return render(request, 'answers.html',{'question':questions[realid], 'answers': answers})


def new_questions(request):
    question_list = questions
    page_questions, paginator = paginate(question_list, request)
    return render(request, 'questions.html', {'questions': page_questions,
                                              'title': 'New questions',
                                              })

def hot_questions(request):
    question_list = sorted(questions, key=itemgetter('likes'), reverse=True)
    page_questions, paginator = paginate(question_list, request)
    return render(request, 'questions.html', {'questions': page_questions,
                                              'title': 'Hot questions',
                                              })

def tags_question(request, tag):
    tmp_questions = []
    for question in questions:
        if tag in question['tags']:
            tmp_questions.append(question)
    question_list = tmp_questions
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