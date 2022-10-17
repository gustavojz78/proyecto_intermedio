from django.urls import path
from appblog.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("bienvenida/", bienvenida, name="entrar"),
    path("user/", user, name="usuario"),
    path("libros/", book, name="libro"),
    path("comentarios/", comment, name="comentario"),
    path("comentarioFormulario/", comentarioFormulario, name="comentarioFormulario"),
    path("libroFormulario/", libroFormulario, name="libroFormulario"),
    path("busquedaAutor/", busquedaAutor, name="busquedaAutor"),
    path("buscar/", buscar,),
    path("usuarioFormulario/", usuarioFormulario, name="usuarioFormulario"),
    path("busquedaComentario/", busquedaComentario, name="busquedaComentario"),
    path("buscarComentario/", buscarComentario,),
    path("busquedaUsuario/", busquedaUsuario, name="busquedaUsuario"),
    path("buscarUsuario/", buscarUsuario,),


 ]
    

