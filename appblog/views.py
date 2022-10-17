from django.http import HttpResponse
from django.shortcuts import render
from appblog.models import *
from appblog.forms import *

def inicio(request):
     return render(request, "appblog/index.html")

def bienvenida(request):
    return render(request, "appblog/bienvenida.html")

def user(request):
    users= Usuario.objects.all()
    return render(request, "appblog/usuarios.html",{'users':users})


def book(request):
    books= Libro.objects.all()
    return render(request, "appblog/libros.html",{'books':books})

def comment(request):
    comments= Comentario.objects.all()
    return render(request, "appblog/comentarios.html",{'comments':comments})

def libroFormulario(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro (titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], fechaIngreso=informacion["fechaIngreso"])
            libro.save()
            return render(request, "appblog/index.html")
    else:
            
     miFormulario = LibroFormulario()
        
    return render(request, "appblog/libroFormulario.html", {"miFormulario":miFormulario})

def busquedaAutor(request):
    return render(request, "appblog/busquedaAutor.html")
    
    
def buscar(request):
    if request.GET["autor"]:
    
        autor = request.GET["autor"]
        libros = Libro.objects.filter(autor__icontains=autor)
        
        return render(request, "appblog/resultadosBusquedasAutor.html", {"libros":libros, "autor":autor})
    else:
        
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

def usuarioFormulario(request):
    if request.method == "POST":
        miFormulario2 = UsuarioFormulario(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data
            usuario =  Usuario (nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], nickname=informacion["nickname"], email=informacion["email"], fechaRegistro=informacion["fechaRegistro"] )
            usuario.save()
            return render(request, "appblog/index.html")
    else:
            
     miFormulario2 = UsuarioFormulario()
        
    return render(request, "appblog/usuarioFormulario.html", {"miFormulario2":miFormulario2})

def busquedaUsuario(request):
    return render(request, "appblog/busquedaUsuario.html")
    
    
def buscarUsuario(request):
    if request.GET["nickname"]:
    
        nickname = request.GET["nickname"]
        usuarios = Usuario.objects.filter(nickname__icontains=nickname)
        
        return render(request, "appblog/resultadosBusquedasUsuario.html", {"usuarios":usuarios, "nickname":nickname})
    else:
        
        respuesta = "No enviaste nickname"
    
    return HttpResponse(respuesta)
    

    
