from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Libro
#from .serializers import LibroSerializer
from .serializers import LibroSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_libro(request):
    ###
    #Lista de todos los libros
    ###
    if request.method == 'GET':
        libro = Libro.objects.all()
        serializer = LibroSerializers(libro, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_libro(request, id):
    """
    Get, update, o delete de un libro en particular
    """
    try:
        libro = Libro.objects.get(isbn=id)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LibroSerializers(Libro)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser(). parse(request)
        serializer = LibroSerializers(libro, data=data)      
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


