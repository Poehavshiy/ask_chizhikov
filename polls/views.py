from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from polls.models import *
from django.http import Http404



def paginate(objects_list, request):
    paginator = Paginator(objects_list, 10)
    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        objects_page = paginator.page(1)
    except EmptyPage:
        objects_page = paginator.page(paginator.num_pages)
    return objects_page, paginator


def username_present(login):
    if User.objects.filter(username=login).exists():
        return False
    return True


def id_question(request, id):
    realid = int(id)
    question = None
    try:
        question = Question.objects.by_id(realid)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    answers_list = Answer.objects.by_id(realid)
    page_answers, paginator = paginate(answers_list, request)
    tags_list=Tag.objects.get_all()
    return render(request, 'answers.html', {'question': question, 'answers': page_answers,
                                            'tags': tags_list})


def new_questions(request):
    question_list = Question.objects.new()
    page_questions, paginator = paginate(question_list, request)
    tags_list=Tag.objects.get_all()
    return render(request, 'questions.html', {'questions': page_questions,
                                              'title': 'New questions',
                                              'tags': tags_list
                                              })


def hot_questions(request):
    question_list = Question.objects.hot()
    page_questions, paginator = paginate(question_list, request)
    tags_list=Tag.objects.get_all()
    return render(request, 'questions.html', {'questions': page_questions,
                                             'title': 'Hot questions',
                                              'tags': tags_list
                                              }
                  )


def tag_questions(request, id):
    tagId = int(id)
    question_list = Question.objects.by_tag(tagId)
    page_questions, paginator = paginate(question_list, request)
    tags_list=Tag.objects.get_all()
    return render(request, 'questions.html',
                  {'questions': page_questions,'title': str(tagId), 'tags': tags_list})


def signup(request):
    if 'submit' in request.POST:
        #
        message = ""
        if username_present(login=request.POST["login"]) == True:
            message += "User is already exists"
        else:
            user = User.objects.create_user(username=request.POST["login"],
                                            email=request.POST["email"], password=request.POST["password"])
            user.save()
            login = request.POST["login"]
            profle = UserProfile.objects.create_profile(author=user,
                                                        nickname=request.POST["nickname"],
                                                        image=request.POST["image"])
            profle.save()
            nickname = request.POST["nickname"]

            message += "User login=" + login + " User nickname=" + nickname + " created."

        return render(request, 'registration.html', {
            "message": message
        })

    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')
