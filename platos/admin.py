from django.contrib import admin
from .models import Platos


# Register your models here.

@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', "precio", "procedencia")
    search_fields = ('nombre', 'precio', 'procedencia')
