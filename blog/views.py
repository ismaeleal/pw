from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from .forms import RegForm
from .forms import iniForm
from .forms import entradaForm
from .forms import cometaForm
from .models import UserProfile
from .models import comentarios
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout




class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 6
    context_object_name = "post_list"

    def get_queryset(self, **kwargs):
        return Post.objects.filter(presentar=True).order_by("-publicado")





    
def PostDetailView(request, slug):
	mensaje = Post.objects.get(slug=slug)
	comentario = comentarios.objects.filter(Post=mensaje)
       
	return render(request, "post_detail.html", {'post':mensaje, 'comentarios':comentario})




def registroView(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("nombre")
		abc2 = form_data.get("email")
		abc3 = form_data.get("usuario")
		acb4 = form_data.get("contraseña")
		
		obj = User.objects.create_user(first_name=abc, email=abc2, username=abc3, password=acb4)
		obj.save()
	context = {
		"el_form":form,

	}

	return render(request, "registro.html",context)

def iniView(request):
	form = iniForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		
		abc3 = form_data.get("usuario")
		acb4 = form_data.get("contraseña")
		
		obj = authenticate( username=abc3, password=acb4)
		if obj is not None:
			if obj.is_active:
				login(request, obj)
				return HttpResponseRedirect("/")
			
		else:
			return HttpResponseRedirect("/no_valido")

	context = {
		"el_form1":form,

	}

	return render(request, "inicio.html",context,)




def entradaView(request):
	form = entradaForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("titulo")
		abc2 = form_data.get("cuerpo")
		abc3 = request.user
		obj = Post.objects.create(titulo=abc, cuerpo=abc2, autor=abc3)
	context = {
		"el_form":form,
	}

	return render(request, "entrada.html",context)


def comeView(request, slug):
	form = cometaForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("comentario")
		abc2 = Post.objects.get(slug=slug)
		abc3 = request.user
		obj = comentarios.objects.create(texto=abc, Post=abc2, autor=abc3)
	context = {
		"el_form":form,
	}

	return render(request, "comentario.html",context)



def logoutView(request):
    logout(request)


    return HttpResponseRedirect("/")

def volverView(request):
    


    return HttpResponseRedirect("/")
def novalidoView(request):
    


     return render(request, 'usuario_no_valido.html')
