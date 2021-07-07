from django.shortcuts import render, redirect
from django.template import loader
from .models import Carrousel
from .models import Usuario
from .forms import UsuarioForm
from .models import Libro
from .forms import LibroForm

def home(request):
    obj = Carrousel.objects.all()
    context = {
        'obj':obj
    }

    return render(request, 'core/home.html', context)

def usuarios(request):
    usuarios = Usuario.objects.all()
    datos = {
        'usuarios': usuarios
    }
    return render(request, 'core/Usuarios.html', datos) 

def form_usuario(request):
    datos = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_usuario.html', datos)

def form_mod_usuario(request, id):
    usuario = Usuario.objects.get(email=id)
    datos = {
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_usuario.html', datos)

def form_del_usuario(request, id):
    usuario = Usuario.objects.get(email=id)
    usuario.delete()
    return redirect(to="Usuarios")

def libros(request):    
    libros = Libro.objects.all()
    datos = {
        'libros': libros
    }
    return render(request, 'core/libros.html', datos)

def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_libro.html', datos)

def form_mod_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    datos = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_libro.html', datos)

def form_del_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    libro.delete()
    return redirect(to="libros")