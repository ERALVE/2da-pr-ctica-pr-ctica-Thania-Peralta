from django.shortcuts import render
from meseros.models import Meseros
from django.db.models import Q, F
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


