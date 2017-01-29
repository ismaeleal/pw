from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


    

         

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    cuerpo = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)
    presentar = models.BooleanField(blank = True, null = False, default=True)
    autor = models.ForeignKey(User)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)


class comentarios(models.Model):
	texto = models.CharField(max_length=200)
	Post = models.ForeignKey(Post)
	autor = models.ForeignKey(User)

	def __str__(self):
		return self.texto
