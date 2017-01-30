from . import views

from django.conf.urls import include, url


app_name = 'accounts'


urlpatterns = [
	# Address
    url(r'^profile_address/$', views.createAddress, name='createAddress'),
    url(r'^delete_address/', views.deleteAddress, name='deleteAddress'),
    url(r'^address_added/$', views.createAddressComplete, name='addressAdded'),
    url(r'^address_edit/(?P<id>[0-9]+)/$', views.editAddress, name='editAddress'),
]