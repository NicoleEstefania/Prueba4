from django.db import models
from django.db.models.base import Model

# Create your models here.
class Carrousel(models.Model):
    image = models.ImageField(upload_to='pics/%y/%m/%d')

    def __Str__(self):
        return self.image

# modelo usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.CharField(max_length=50, primary_key=True, verbose_name='Email')
    contrasena = models.CharField(max_length=10, verbose_name='Contrasena')
    comentarios = models.CharField(max_length=20, null=True, blank=True, verbose_name='Comentarios')

    def __str__(self):
        return self.email

# modelo categoria
class Categorias(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

# modelo libro 
class Libro(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True, verbose_name='ISBN')
    nombre = models.CharField(max_length=20, verbose_name='Nombre del libro')
    autor = models.CharField(max_length=20, null=True, blank=True, verbose_name='autor')
    descripcion = models.CharField(max_length=20, null=True, blank=True, verbose_name='descripcion')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn