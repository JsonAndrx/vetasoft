from django.contrib import admin
from django.urls import path
from servicios import views
urlpatterns = [
    path('servicios/citas/', views.citasv, name="citas"),
    path('modificar-citas/<id>/', views.modificar_citas, name="modificar_citas"),
    path('eliminar-citas/<id>/', views.eliminar_cita, name="eliminar_cita"),
    path('servicios/cartonvacunas/', views.carton_vacunas, name="carton"),
    path('modificar-carton/<id>/', views.modificar_carton, name="modificar_carton"),
    path('eliminar-carton/<id>/', views.eliminar_carton, name="eliminar_carton"),
    path('servicios/hospitalizacion/', views.hospitalizacionv, name="hospitalizacion"),
    path('modificar-hospitalizacion/<id>/', views.modificar_hospitalizacion, name="modificar_hospitalizacion"),
    path('eliminar-hospitalizacion/<id>/', views.eliminar_hospitalizacion, name='eliminar_hospitalizacion'),
    path('servicios/recetamedica', views.receta_medicas, name="receta"),
    path('modificar-receta/<id>/', views.modificar_receta, name="modificar_receta"),
    path('eliminar-receta/<id>', views.eliminar_receta, name="eliminar_receta"),
]