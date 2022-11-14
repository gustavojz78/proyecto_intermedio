from django.urls import path
from appblog import views
from django.contrib.auth.views import *


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.bienvenida, name="entrar"),
    path("login/", views.login_request, name="Login"),
    path("registro/", views.register_request, name="Registro"),
    path("perfil/", views.Perfil, name="Perfil"),
    path("logout/", LogoutView.as_view(template_name="appblog/logout.html"), name="Logout"), 
    path("editarPerfil/", views.editarPerfil ,name="EditarPerfil"),
    path("user/", views.user, name="usuario"),
    path("comentarios/", views.comment, name="comentario"),
    path("comentarioFormulario/", views.comentarioFormulario, name="comentarioFormulario"),
    path("libroFormulario/", views.libroFormulario, name="libroFormulario"),
    path("busquedaAutor/", views.busquedaAutor, name="busquedaAutor"),
    path("buscar/", views.buscar,),
    path("busquedaComentario/", views.busquedaComentario, name="busquedaComentario"),
    path("buscarComentario/", views.buscarComentario,),
    path("busquedaUsuario/", views.busquedaUsuario, name="busquedaUsuario"),
    path("buscarUsuario/", views.buscarUsuario,),
    path("borrarComentario/<comentario_id>/", views.eliminarComentario, name="eliminarComentario"),
    path("editarComentario/<comentario_id>/", views.actualizarComentario, name="editarComentario"),
    path("books/lista", views.LibroLista.as_view(), name="libro_lista"),
    path("nuevo/", views.LibroCrear.as_view(), name="Nuevo"),
    path("<pk>/", views.LibroDetalle.as_view(), name="Ver"),
    path("editar/<pk>", views.LibroMdificar.as_view(), name="Editar"),
    path("borrar/<pk>", views.LibroBorrar.as_view(), name="Borrar"),
    path("perfil/cambiarContrasenia/", views.CambiarContrasenia.as_view() ,name="CambiarContrasenia"),
    
  
   


 ]
    

