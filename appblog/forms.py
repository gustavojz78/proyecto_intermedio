from datetime import *

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UsuarioFormulario(forms.Form):
#     nombre=forms.CharField(max_length=30)
#     apellido=forms.CharField(max_length=30)
#     dni=forms.IntegerField()
#     nickname=forms.CharField(max_length=30)
#     email=forms.EmailField()
  
class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()
 
class ComentarioFormulario(forms.Form):
    texto = forms.CharField()

class UsuarioRegistroForm(UserCreationForm):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_text = { k: "" for k in fields} 

class UserEditForm(forms.Form):
    first_name= forms.CharField(label="Modificar nombre")
    last_name= forms.CharField(label="Modificar apelido")
    email=forms.EmailField(label="Modificar email")
    imagen = forms.ImageField() 
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','imagen']
        help_text = { k: "" for k in fields} 



    
    
  
    
    