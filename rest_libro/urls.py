from django.urls import path
from rest_libro.views import lista_libro, detalle_libro
from rest_libro.viewlogin import login

urlpatterns =[
    path('lista_libro',lista_libro, name="lista_libro"),
    path('detalle_libro/<id>', detalle_libro, name="detalle_libro"),
    path('login', login, name="login"),
    ]