from . import views

from django.conf.urls import include, url


app_name = 'address'


urlpatterns = [
    # ajax 更新省市区用的
    url(r'^getDistrictList/$', views.getDistrictList, name='getDistrictList'),
]