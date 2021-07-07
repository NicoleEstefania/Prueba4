from django import forms
from django.forms import ModelForm 
from .models import Usuario
from .models import Libro

class UsuarioForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contrasena', 'comentarios',]

class LibroForm(ModelForm):
    
    class Meta:
        model = Libro
        fields = ['isbn', 'nombre', 'autor', 'descripcion','categoria']