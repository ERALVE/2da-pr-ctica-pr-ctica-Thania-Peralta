from django.urls import path
from . import views
from .views import meseros_25

urlpatterns = [

    path('meseros_orm/', views.meseros_orm, name='meseros_orm'),
    path('meseros_orm_edad/', views.meseros_orm_edad, name='meseros_orm_edad'),
    # Examen final
    path('meseros_25/', meseros_25, name='meseros_25'),
    # URL para las vistas basadas en clase
    path('meseros_list_vc/', views.MeserosList.as_view(), name="meseros_list_vc"),
    path('meseros_create_vc/', views.MeserosCreate.as_view(), name="meseros_create_vc"),
    path('meseros_list/', views.Meseros_all_List.as_view(), name='meseros_list'),
    path('meseros_update_vc/<int:pk>/', views.MeserosUpdate.as_view(), name="meseros_update_vc"),
    path('meseros_delete_vc/<int:pk>/', views.MeserosDelete.as_view(), name="meseros_delete_vc"),
#URLs Django Framework drf
    path('meseros_list_drf_def/', views.Meseros_POST_api_view, name="meseros_list_drf_def"),
    path('meseros_detail_drf_def/<int:pk>/', views.editar_meseros, name="meseros_detail_drf_def"),
]