from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import *
from django.views.generic.edit import *

from appblog.forms import *
from appblog.models import *
from django.contrib.auth.models import User


class LibroLista(LoginRequiredMixin,ListView):
    model=Libro
    template_name = "appblog/libro_lista.html"
class LibroCrear(CreateView):
    model = Libro
    #IMPORTANTISIMO despues de appblog/ debe ir el nombre de como van guardado los libros, en este caso es books
    success_url= "/appblog/books/lista"
    fields = ["titulo","autor","genero","fechaIngreso"]
class LibroDetalle(DetailView):
    model = Libro
    template_name = "appblog/libro_detalle.html"
class LibroMdificar(UpdateView):
    model = Libro
    success_url= "/appblog/books/lista"
    fields = ["titulo","autor","genero","fechaIngreso"]
class LibroBorrar(DeleteView):
    model = Libro
    success_url= "/appblog/books/lista"

class CambiarContrasenia(PasswordChangeView):
    template_name = "appblog/cambiarContrasenia.html"
    success_url= "/appblog/perfil/"

@login_required
def inicio(request):
    avatar=Avatar.objects.filter(user=request.user)
    if len(avatar) >0:
        imagen = avatar[0].imagen.url
        return render(request, "appblog/base2.html",{"imagen_url":imagen})
    else:
        return render(request, "appblog/base2.html")


def bienvenida(request):
    return render(request, "appblog/bienvenida.html")

def user(request):
    users= User.objects.all()
    return render(request, "appblog/usuarios.html",{'users':users})

def comment(request):
    comments= Comentario.objects.all()
    return render(request, "appblog/comentarios.html",{'comments':comments})

def book(request):
    books= Libro.objects.all()
    return render(request, "appblog/libros.html",{'books':books})


@login_required
def libroFormulario(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro (titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], fechaIngreso=datetime.now())
            libro.save()
            return render(request, "appblog/index.html")
    else:        
     miFormulario = LibroFormulario()   
    return render(request, "appblog/libroFormulario.html", {"miFormulario":miFormulario})

@login_required
def comentarioFormulario(request):
    if request.method == "POST":
        miFormulario3 = ComentarioFormulario(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid:
            informacion = miFormulario3.cleaned_data
            comentario = Comentario (creador=request.user, texto=informacion["texto"], fechaCreacion=datetime.now())
            comentario.save()
            return render(request, "appblog/base2.html")
    else:        
        miFormulario3 = ComentarioFormulario()
    return render(request, "appblog/comentarioFormulario.html", {"miFormulario3":miFormulario3})

def busquedaAutor(request):
    return render(request, "appblog/busquedaAutor.html")
    
def busquedaUsuario(request):
    return render(request, "appblog/busquedaUsuario.html")   
    
def busquedaComentario(request):
    return render(request, "appblog/busquedaComentario.html")


def buscarUsuario(request):
    if request.GET["username"]:
        username = request.GET["username"]
        usuarios = User.objects.filter(username__icontains=username)
        return render(request, "appblog/resultadosBusquedasUsuario.html", {"usuarios":usuarios, "username":username})
    else:   
        respuesta = "No enviaste Alias"
    return HttpResponse(respuesta)
    

def buscar(request):
    if request.GET["autor"]:
        autor = request.GET["autor"]
        libros = Libro.objects.filter(autor__icontains=autor)
        return render(request, "appblog/resultadosBusquedasAutor.html", {"libros":libros, "autor":autor})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
    

def buscarComentario(request):
    if request.GET["creador"]:
        creador = request.GET["creador"]
        comentarios = Comentario.objects.filter(creador__icontains=creador)
        return render(request, "appblog/resultadosBusquedasComentarios.html", {"comentarios":comentarios, "creador":creador})
    else:
        respuesta = "No enviaste creador"
    return HttpResponse(respuesta)
    

@login_required   
def eliminarComentario (request, comentario_id):
    try:
        comentario=Comentario.objects.get(id=comentario_id)
        comentario.delete()
        return render(request, "appblog/base2.html") 
    except Exception as exc:
        return render(request, "appblog/base2.html") 


@login_required
def actualizarComentario (request, comentario_id):
    comentario=Comentario.objects.get(id=comentario_id)
    if request.method == "POST":
        miFormulario3 =ComentarioFormulario(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid:
            info=miFormulario3.cleaned_data
            comentario.texto=info['texto']
            comentario.save()
            return redirect("inicio")      
    else:
        miFormulario3= ComentarioFormulario(initial={"creador":comentario.creador,"texto":comentario.texto} )
        return render(request, "appblog/editarComentario.html", {"miFormulario3":miFormulario3, "comentario_id":comentario_id})


def login_request(request):
    if request.method =="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=usuario, password=contra)  
            if usuario is not None:
                login(request,usuario)
                avatar,nuevo=Avatar.objects.get_or_create(user=request.user)
                return render(request, "appblog/base2.html",{"mensaje":[f"Bienvenid@!!!"]})
            else:
                return render(request, "appblog/index.html",{"mensaje": ["Usuario no valido"]})
        else:
                return render(request, "appblog/index.html",{"mensaje": ["Error: Datos Incorrectos"]})
    form=AuthenticationForm()
    return render(request,"appblog/login.html", {"form":form})


def register_request(request):
    if request.method == "POST":
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            print(username) 
            form.save()
            return render(request, "appblog/index.html", {"mensaje": [f"El usuario '{username}' fue creado con EXITO"]})
        else:
            return render(request, "appblog/index.html",{"mensaje": [" Password NO VALIDO"]} )
    else:
        form= UsuarioRegistroForm()
    return render(request, "appblog/registro.html", {"form": form})


def Perfil(request):
    return render(request, "appblog/perfil.html", {})


@login_required
def editarPerfil (request):
    usuario = request.user
    if request.method == "POST":
        forms =UserEditForm(request.POST,request.FILES)
        if forms.is_valid():
            info=forms.cleaned_data
            usuario.first_name=info['first_name']
            usuario.last_name=info['last_name']
            usuario.email=info['email']
            usuario.avatar.imagen=info['imagen']
            usuario.avatar.save()
            usuario.save()     
        return render(request,"appblog/index.html")  
    else:
        forms= UserEditForm(initial={
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            "email":usuario.email,
            "imagen":usuario.avatar.imagen})
        return render(request, "appblog/editarPerfil.html", {"forms":forms, "usuario":usuario})

