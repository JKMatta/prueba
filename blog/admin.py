from django.contrib import admin
from .models import Post, Comment, AdoptarRescatado

admin.site.register(Post)
admin.site.register(AdoptarRescatado)
admin.site.register(Comment)