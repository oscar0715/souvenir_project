from . import views

from django.conf.urls import include, url


app_name = 'accounts'


urlpatterns = [
	# 获取 Signin form
    url(r'^getSignInForm/$', views.getSignInForm, name='getSignInForm'),
]