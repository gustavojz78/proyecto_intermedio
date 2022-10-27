from django.db import models


class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField(primary_key=True)
    nickname=models.CharField(max_length=30)
    email=models.EmailField()
    fechaRegistro=models.DateTimeField()

    def __str__(self):
        return f"{(self.nombre)}-{(self.apellido)} | {(self.dni)}" 


class Libro(models.Model):
    titulo=models.CharField(max_length=80)
    autor=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    fechaIngreso=models.DateTimeField()

    def __str__(self):
        return f"Titulo:{(self.titulo)} | Autor:{(self.autor)} | Genero:{(self.genero)} | fechaIngreso:{(self.fechaIngreso.strftime('%d %b, %Y'))}"   ##.strftime('%d %b, %Y')

class Comentario(models.Model):
    id=models.IntegerField(primary_key=True)
    creador=models.CharField(max_length=30)
    texto=models.CharField(max_length=5000)
    fechaCreacion=models.DateTimeField()

    def __str__(self):
        return f"{(self.id)}-{(self.creador)} | {(self.fechaCreacion.strftime('%d %b, %Y'))}"
