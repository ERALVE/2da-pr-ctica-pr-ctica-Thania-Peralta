from django.shortcuts import render
from clientes.models import Clientes

# Create your views here.
def clientes_list(request):
        data_context = Clientes.objects.all()
        return render(request, 'clientes_list.html', context={'data': data_context})
