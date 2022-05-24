from django.contrib import admin
from django.urls import path
from usuarios import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/pacientes/', views.pacientesv, name="pacientes"),
    path('usuarios/veterinarios/', views.veterinarios, name="veterinarios"),
    path('usuarios/propietario/', views.propietarios, name="propietario"),
    path('modificar-pacientes/<id>/', views.modificar_paciente, name="modificar_pacientes"),
    path('eliminar-pacientes/<id>/', views.eliminar_paciente, name="eliminar_pacientes"),
    path('moficar-propietario/<id>/', views.modificar_propietario, name="modificar_propietario"),
    path('eliminar-propietario/<id>/', views.eliminar_propietario, name="eliminar_propietario"),
    path('modificar-veterinario/<id>/', views.modificar_veterinario, name="modificar_veterinario"),
    path('eliminar-veterinario/<id>/', views.eliminar_veterinario, name="eliminar_veterinario"),
    path('home/', views.home, name='home'),
]