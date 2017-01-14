from . import views

from django.conf.urls import include, url


app_name = 'posts'


urlpatterns = [

    # 旧代码 url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.newPost, name='new'),
    url(r'^getDistrictList/$', views.getDistrictList, name='getDistrictList'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]