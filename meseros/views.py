from django.shortcuts import render
from meseros.models import Meseros

# Create your views here.
def meseros_list(request):
        data_context = Meseros.objects.all()
        return render(request, 'meseros_list.html', context={'data': data_context})


