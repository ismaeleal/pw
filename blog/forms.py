from django import forms 

class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()
	usuario = forms.CharField(max_length=100)
	contraseña = forms.CharField(widget=forms.PasswordInput)


class iniForm(forms.Form):
	
	usuario = forms.CharField(max_length=100)
	contraseña = forms.CharField(widget=forms.PasswordInput)

class entradaForm(forms.Form):
	titulo = forms.CharField(max_length=200)
	cuerpo = forms.CharField(widget=forms.Textarea)

class cometaForm(forms.Form):
	comentario = forms.CharField(widget=forms.Textarea)