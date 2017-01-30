from django.contrib import admin

from .models import District,Country,UserAddress

# Register your models here.

admin.site.register(District)
admin.site.register(Country)
admin.site.register(UserAddress)