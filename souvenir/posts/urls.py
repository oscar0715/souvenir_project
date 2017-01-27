from . import views

from django.conf.urls import include, url


app_name = 'posts'


urlpatterns = [
	# 新建一个 Post
    url(r'^new/$', views.newPost, name='new'),
    
    # 所有 Post
    url(r'^$', views.IndexView.as_view(), name='index'),

    # 用户的Post
    url(r'^userposts/$', views.UserPostListView.as_view(), name="userposts"),
    
    # 查看某个post的详细列表
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # 申请一张 Postcard
    url(r'^claim/$', views.claim, name='claim'),


]