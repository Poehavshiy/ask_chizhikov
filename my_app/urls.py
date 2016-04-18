from django.conf.urls import url

from . import views
#url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
urlpatterns = [
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.login, name='login'),
    url(r'^ask', views.ask, name='ask'),
    url(r'^question/(?P<id>\d+)', views.id_question, name='id_question'),
    url(r'^/?', views.new_questions, name='new_questions'),
    url(r'^hot', views.hot_questions, name='hot_questions'),
    url(r'^tag/(?P<tag>\w+)', views.tags_question, name='tag_questions'),
]
