from django.conf.urls import url

from post import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list, name='main'),

    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]