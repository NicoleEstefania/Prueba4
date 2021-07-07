from django.urls import path
from .views import home, usuarios, form_usuario, form_mod_usuario, form_del_usuario, libros, form_libro, form_mod_libro, form_del_libro

urlpatterns = [
    path('', home, name="home"),
    path('Usuarios', usuarios, name="usuarios"),
    path('form-usuario', form_usuario, name="form_usuario"),
    path('form-mod-usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
    path('form-del-usuario/<id>', form_del_usuario, name="form_del_usuario"),
    path('libros', libros, name="libros"),
    path('form-libro', form_libro, name="form_libro"),
    path('form-mod-libro/<id>', form_mod_libro, name="form_mod_libro"),
    path('form-del-libro/<id>', form_del_libro, name="form_del_libro"),
]