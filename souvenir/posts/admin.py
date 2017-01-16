from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    readonly_fields = ('modified',)

admin.site.register(Post, PostAdmin)