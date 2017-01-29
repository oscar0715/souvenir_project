from . import views

from django.conf.urls import include, url


app_name = 'accounts'


urlpatterns = [
	# Address
    url(r'^profile_address/$', views.createAddress, name='createAddress'),
    url(r'^delete_address/', views.deleteAddress, name='delete_address'),
    url(r'^address_added/$', views.createAddressComplete, name='address_added'),

    
]