from django.contrib import admin

# Register your models here.
from .models import Post, comentarios

admin.site.register(Post)

admin.site.register(comentarios)
