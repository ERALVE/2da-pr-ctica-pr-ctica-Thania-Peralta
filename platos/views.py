from django.shortcuts import render
from platos.models import Platos
from django.db.models import Q


# Create your views here.
def platos_list(request):
        #data_context = Platos.objects.all()
        data_context= []
        """En esta parte del codigo vamos agregar platos con precios mayores a 40 soles"""
        #platos = Platos(nombre="pachamanca", precio=60, procedencia="Peruana")
        #platos.save()

        return render(request, 'platos_list.html', {'data': data_context})
def platos_orm(request):
        data_context = []
        """En esta parte del codigo vamos agregar platos con precios mayores a 40 soles"""
        #platos = Platos(nombre="pachamanca", precio=60, procedencia="Peruana")
        #platos.save()
        """Query"""
        query = Q(procedencia__startswith= "Per") | Q(precio=40)
        data_context = Platos.objects.filter(query, precio__gt=40)
        return render(request, 'platos_orm.html', {'data': data_context})
def platos_orm_delet(request):


        """Eliminar los platos con precios menores a 15 soles"""

        data_context = Platos.objects.filter(precio__lt=15)

        data_context.delete()
        data_context = Platos.objects.all()

        # data_context = []
        # """En esta parte del codigo vamos agregar platos con precios mayores a 40 soles"""
        # platos = Platos(nombre="Huevo frito con arroz", precio=10, procedencia="Peruana")
        # platos.save()

        return render(request, 'platos_orm_delet.html', {'data': data_context})

