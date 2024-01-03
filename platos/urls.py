from django.urls import path
from . import views
from .views import platos_50

urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_orm/', views.platos_orm, name='platos_orm'),
    path('platos_orm_delet/', views.platos_orm_delet, name='platos_orm_delet'),
#Examen final
    path('platos_50/', platos_50, name='platos_50'),
]