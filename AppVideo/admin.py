from django.contrib import admin
from .models import streamVideo, comments, likes

# Register your models here.

admin.site.register(streamVideo)
admin.site.register(comments)
admin.site.register(likes)