from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils import timezone

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured

# Create your models here.
class AnswerManager(models.Manager):
    @staticmethod
    def by_id(id):
        return Answer.objects.filter(question=id)


class QuestionManager(models.Manager):
    @staticmethod
    def new():
        return Question.objects.order_by('-added_at')

    @staticmethod
    def hot():
        return Question.objects.order_by('-rating')

    @staticmethod
    def by_tags(tag):
        return Question.objects.filter(tags__title=tag)

    @staticmethod
    def by_id(q_id):
        return Question.objects.get(id=q_id)


class registrHandler:
    def __init__(self, login, email, nickname, password, image):
        self.login = login
        self.email = email
        self.nickname = nickname
        self.password = password
        self.image = image

    def get_login(self):
        return self.login

    def get_email(self):
        return self.email

    def get_nickname(self):
        return self.email

    def get_password(self):
        return self.password

    def get_image(self):
        return self.image


class UserProfileManager(models.Manager):
    def create_profile(self, author, nickname, image):
        user = self.create(
                author = author,
                nickname=nickname,
                image=image
        )
        # do something with the book
        return user


class Tag(models.Model):
    title = models.CharField(max_length=128)


class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name='likes_users')
    manager = QuestionManager


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    added_at = models.DateTimeField(default=timezone.now)
    manager = AnswerManager

#enhansment of Djangouser
class UserProfile(models.Model):
    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    #2 additionsl fields
    nickname = models.CharField(max_length=128)
    image = models.CharField(max_length=128)

    objects = UserProfileManager()


class QuestionTest(models.Model):
    question_text = models.CharField(max_length=200)
