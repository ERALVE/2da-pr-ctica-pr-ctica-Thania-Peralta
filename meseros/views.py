from django.shortcuts import render
from meseros.models import Meseros
from django.db.models import Q, F
#serealización
from .serializers import MeserosSerializer
#VBC
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from meseros.forms import MeserosForm
#Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def meseros_list(request):
        data_context = Meseros.objects.all()
        return render(request, 'meseros_list.html', context={'data': data_context})

def meseros_orm(request):
        """Query"""
        query = Q(pais__startswith= "Per") | Q(edad=30)
        data_context = Meseros.objects.filter(query, edad__lt=30)
        return render(request, 'meseros_orm.html', {'data': data_context})

def meseros_orm_edad(request):
        """Se incrementara la edad de los meseros cada qye se use la url"""
        Meseros.objects.filter(edad__gte=16).update(edad=F('edad')+ 5)
        data_context = Meseros.objects.all()

        return render(request, 'meseros_orm_edad.html', {'data': data_context})
"""Examen Final"""

@api_view(['GET'])
def meseros_25(request):
    meseros_25 = Meseros.objects.filter(edad__gt=25)
    serializer = MeserosSerializer(meseros_25, many=True)
    return Response(serializer.data)

#Meseros peruanos
class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros_list_vc.html'
    context_object_name = 'meseros'

    def get_queryset(self):
        return Meseros.objects.filter(pais='Perú')

# Ingreso de datos nuevos
class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_create.html'
    success_url = reverse_lazy('meseros_list')

#Lista de todos los datos de la BD
class Meseros_all_List(ListView):
    model = Meseros
    template_name = 'meseros_list.html'
    context_object_name = 'meseros'

    def get_queryset(self):
        return Meseros.objects.all()

class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_update_vc.html'
    success_url = reverse_lazy('meseros_list')

class MeserosDelete(DeleteView):
    model = Meseros
    template_name = "meseros_delete_vc.html"
    success_url = reverse_lazy('meseros_list')

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def Meseros_POST_api_view(request):

    if request.method == 'POST':
        print("Data MESEROS: {}".format(request.data))
        """objeto jason"""
        serializers_class = MeserosSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.data, status=status.HTTP_400_BAD_REQUEST )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def editar_meseros(request, pk):
    meseros = Meseros.objects.filter(id=pk).first()

    if meseros:
        if request.method == 'GET':
            serializers_class = MeserosSerializer(meseros)
            return Response(serializers_class.data)

        elif request.method == 'DELETE':
            print("Ingreso a DELETE")
            meseros.delete()
            return Response("El mesero ha sido eliminado de la base de datos", status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = MeserosSerializer(meseros, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Mesero no encontrado"}, status=status.HTTP_404_NOT_FOUND)
