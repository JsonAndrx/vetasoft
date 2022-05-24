from django.urls import path
from inventariado import views
urlpatterns = [
    path('inventariado/inventarios/', views.inventariosv, name="inventarios"),
    path('inventariado/medicinas/', views.medicinav, name="medicina"),
    path('iventariado/vacunas/', views.vacunasv, name="vacunas"),
    path('modificar-vacuna/<id>/', views.modificar_vacuna, name="modificar_vacuna"),
    path('eliminar-vacuna/<id>/', views.eliminar_vacuna, name="eliminar_vacuna"),
    path('modificar-medicina/<id>/', views.modificar_medicina, name="modificar_medicina"),
    path('eliminar-medicina/<id>/', views.eliminar_medicina, name="eliminar_medicina"),
    path('moficiar-inventario/<id>/', views.modificar_inventario, name="modificar_inventario"),
    path('eliminar-inventario/<id>/', views.eliminar_inventario, name="eliminar_inventario"),
]