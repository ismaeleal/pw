from django.contrib import admin

# Register your models here.
from .models import Post, UserProfile, comentarios

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(comentarios)