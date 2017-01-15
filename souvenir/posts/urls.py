from . import views

from django.conf.urls import include, url


app_name = 'posts'


urlpatterns = [
	# 新建一个 Post
    url(r'^new/$', views.newPost, name='new'),

    # ajax 更新省市区用的
    url(r'^getDistrictList/$', views.getDistrictList, name='getDistrictList'),
    
    # 所有 Post
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # 查看某个post的详细列表
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]