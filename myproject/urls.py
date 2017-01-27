"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  include, url
from django.contrib import admin
import blog.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.PostList.as_view(), name='home'),
    url(r'^registro/$', views.registroView, name='registro'),
    url(r'^inicio/$', views.iniView, name='inicio'),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.PostDetailView, name='post'),
	url(r'^entrada/$', views.entradaView, name='entrada'),
	url(r'^posts/(?P<slug>[-\w]+)/add-coment/$', views.comeView, name='nuevo_comentario'),
	url(r'^cerrar/$', views.logoutView, name='logout'),
	url(r'^volver/$', views.volverView, name='volver'),
	url(r'^no_valido/$', views.novalidoView, name='novalido'),


]
