from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils import timezone


# Create your models here.
class AnswerManager(models.Manager):
    def by_id(self, id):
        return Answer.objects.filter(question=id)

class TagsManager(models.Manager):
    def by_question(self, q_id):
        return Tag.objects.filter(id = q_id)
    def get_all(self):
        return Tag.objects.order_by('id')

class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at')
    def hot(self):
        return Question.objects.order_by('-rating')
    def by_id (self,q_id):
        return Question.objects.get(id=q_id)
    def by_tag (self,tag_id):
        #tags = Tag.objects.get(title__contains = 'YxA%')
        return Question.objects.filter(tag = tag_id)


class UserProfileManager(models.Manager):
    def create_profile(self, author, nickname, image):
        user = self.create(
                author=author,
                nickname=nickname,
                image=image
        )
        # do something with the book
        return user


class Tag(models.Model):
    title = models.CharField(max_length=128)

    objects = TagsManager()


class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag)

    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    added_at = models.DateTimeField(default=timezone.now)
    objects = AnswerManager()


# enhansment of Djangouser
class UserProfile(models.Model):
    author = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            primary_key=True
    )
    # 2 additionsl fields
    nickname = models.CharField(max_length=128)
    image = models.CharField(max_length=128)

    objects = UserProfileManager()


class QuestionTest(models.Model):
    question_text = models.CharField(max_length=200)
