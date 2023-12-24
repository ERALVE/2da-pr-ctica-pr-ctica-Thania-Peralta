from django.shortcuts import render
from platos.models import Platos


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
        # platos = Platos(nombre="pachamanca", precio=60, procedencia="Peruana")
        # platos.save()
        return render(request, 'platos_orm.html', {'data': data_context})
