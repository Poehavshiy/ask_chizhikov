from django.core.management.base import BaseCommand, CommandError
from polls.models import Question, Tag, Answer, UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import random
import string


def randstring(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])


def randomQuestionGenerator(users, tags):
    user = User.objects.get(id=random.randint(1, users - 1))
    filename = "/home/nikita/web/ask_chizhikov/polls/management/commands/" + "q" + str(random.randint(1, 5)) + ".txt"
    f = open(filename, 'r')
    title = ""
    text = ""
    help = 0

    for line in f:
        if line == "\n":
            help = 1
        if help == 0:
            title += line
        else:
            text += line
    added_at = parse_datetime("2012-02-21 10:28:45")

    #####
    q = Question(author=user, text=text, title=title, rating=random.randint(0, 50), added_at=added_at,
                 answers=random.randint(0, 1000))
    q.save()
    for i in range(0, 5):
        random_tag_id = random.randint(1, tags-1)
        q.tag.add(Tag.objects.get(id=random_tag_id))

    q.save()


def randomAnswerGenerator(users, questions):
    user = User.objects.get(id=random.randint(1, users))
    q = Question.objects.get(id=random.randint(1, questions))
    filename = "/home/nikita/web/ask_chizhikov/polls/management/commands/" + "a" + str(random.randint(1, 10)) + ".txt"
    f = open(filename, 'r')
    text = ""
    for line in f:
        text += line

    a = Answer(author=user, text=text, question=q)
    a.save()


def randomUserGenerator():
    user = User.objects.create_user(username=randstring(10), email=randstring(20), password=randstring(30))
    user.save()
    profle = UserProfile.objects.create_profile(author=user,
                                                nickname=randstring(20),
                                                image=randstring(20))
    profle.save()


def TagGenerator():
    filename = "/home/nikita/web/ask_chizhikov/polls/management/commands/tags.txt"
    f = open(filename, 'r')
    for line in f:
        t = Tag(title=line)
        t.save()


def filling(tags, users, questions, answers):
    TagGenerator()
    for i in range(0, users):
        randomUserGenerator()
    for i in range(0, questions):
       randomQuestionGenerator(users, tags)
    for i in range(0, answers):
        randomAnswerGenerator(users, questions)


filling(10, 20, 200, 400)
