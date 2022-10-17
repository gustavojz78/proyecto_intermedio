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
        print(type(self.fechaIngreso))
        return f"titulo:{self.titulo}-autor:{self.autor} | genero:{self.genero} | fechaIngreso:{self.fechaIngreso.strftime('%d %b, %Y')}"   ##{{libro.autor}}. Titulo: {{libro.titulo}}. {{libro.genero}}. Subido al blog el dia: {{libro.fechaIngreso}}

class Comentario(models.Model):
    id=models.IntegerField(primary_key=True)
    creador=models.CharField(max_length=30)
    texto=models.CharField(max_length=5000)
    fechaCreación=models.DateTimeField()
