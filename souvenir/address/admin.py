from django.contrib import admin

from .models import District,Country,User_Address

# Register your models here.

admin.site.register(District)
admin.site.register(Country)
admin.site.register(User_Address)