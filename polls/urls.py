from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.login, name='login'),
    url(r'^ask', views.ask, name='ask'),
    url(r'^question/(?P<id>\d+)', views.id_question, name='id_question'),
    url(r'^tag/(?P<id>\d+)', views.tag_questions, name='tag_questions'),
    url(r'^hot', views.hot_questions, name='hot_questions'),
    url(r'^/?', views.new_questions, name='new_questions')
]
