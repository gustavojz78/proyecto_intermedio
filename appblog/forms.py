from datetime import *
from django import forms

class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    dni=forms.IntegerField()
    nickname=forms.CharField(max_length=30)
    email=forms.EmailField()
    fechaRegistro=forms.DateTimeField()

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()
    fechaIngreso = forms.DateTimeField()


class ComentarioFormulario(forms.Form):
    creador = forms.CharField()
    texto = forms.CharField()
    
  
    
    