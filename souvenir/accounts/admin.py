from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import MyProfile

import logging

logger = logging.getLogger(__name__)

# Register your models here.
admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = MyProfile
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = [ ProfileInline, ]
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

logging.debug("[accounts.admin] = " + "Here")
admin.site.register(User, CustomUserAdmin)