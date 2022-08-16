from django.contrib import admin
from .models import Location, Post
# Register your models here.

admin.site.register(Location)  #註冊至Administration(管理員後台)
admin.site.register(Post)  #註冊至Administration(管理員後台)
