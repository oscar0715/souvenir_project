from . import views

from django.conf.urls import include, url


app_name = 'accounts'


urlpatterns = [

    url(r'^profile_address/$', views.createAddress, name='createAddress'),
]