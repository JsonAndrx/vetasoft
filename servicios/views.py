from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import agendamiento_citas, carton_vacuna, hospitalizacion, receta_medica
from .forms import FormularioCarVa, FormularioCitas, FormularioHospi, FormularioReceta
# Create your views here.

@login_required
def citasv(request):
    data = {
        'cita':agendamiento_citas.objects.all(),
        'formu':FormularioCitas(),
        'mensaje':'OK'}
    if request.method == 'POST':
        formulario = FormularioCitas(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Registro exitoso"
        else:
            data['formu']=formulario
    return render(request, 'servicios/citas.html', data)


@login_required
def modificar_citas(request, id):
    citas = get_object_or_404(agendamiento_citas, id=id)
    data = {'formu': FormularioCitas(instance=citas)}

    if request.method == 'POST':
        formulario = FormularioCitas(data=request.POST, instance=citas)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='citas')
        else:
            data['formu'] = formulario

    return render(request, "servicios/modificar_citas.html", data)

@login_required
def eliminar_cita(request, id):
    citas = get_object_or_404(agendamiento_citas, id=id)
    citas.delete()
    return redirect(to="citas")

@login_required
def carton_vacunas(request):
    data = {
        'carton':carton_vacuna.objects.all(),
        'formu':FormularioCarVa(),
        'mensaje':'OK'}
    if request.method == 'POST':
        formulario = FormularioCarVa(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registro exitoso"
        else:
            data['formu']=formulario

    return render(request, 'servicios/cartonvacu.html', data)


@login_required
def modificar_carton(request, id):
    carton = get_object_or_404(carton_vacuna, id=id)
    data = {'formu': FormularioCarVa(instance=carton)}

    if request.method == 'POST':
        formulario = FormularioCarVa(data=request.POST, instance=carton)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='carton')
        else:
            data['formu'] = formulario

    return render(request, "servicios/modificar_carton.html", data)


@login_required
def eliminar_carton(request, id):
    citas = get_object_or_404(carton_vacuna, id=id)
    citas.delete()
    return redirect(to="carton")   


@login_required
def hospitalizacionv(request):
    data = {
        'hospitalizacion':hospitalizacion.objects.all(),
        'formu':FormularioHospi(),
        'mensaje':'OK'}
    if request.method == 'POST':
        formulario = FormularioHospi(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Registro exitoso"
        else:
            data['formu']=formulario
    return render(request, 'servicios/hospitalizacion.html', data)


@login_required
def modificar_hospitalizacion(request, id):
    citas = get_object_or_404(hospitalizacion, id=id)
    data = {'formu': FormularioHospi(instance=citas)}

    if request.method == 'POST':
        formulario = FormularioHospi(data=request.POST, instance=citas)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='hospitalizacion')
        else:
            data['formu'] = formulario

    return render(request, "servicios/modificar_hospitalizacion.html", data)


@login_required
def eliminar_hospitalizacion(request, id):
    citas = get_object_or_404(hospitalizacion, id=id)
    citas.delete()
    return redirect(to="hospitalizacion")   


@login_required
def receta_medicas(request):
    data = {
        'receta':receta_medica.objects.all(),
        'formu':FormularioReceta(),
        'mensaje':'OK'}
    if request.method == 'POST':
        formulario = FormularioReceta(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Registro exitoso"
        else:
            data['formu']=formulario
    return render(request, 'servicios/receta_medica.html', data)


@login_required
def modificar_receta(request, id):
    citas = get_object_or_404(receta_medica, id=id)
    data = {'formu': FormularioReceta(instance=citas)}

    if request.method == 'POST':
        formulario = FormularioReceta(data=request.POST, instance=citas)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='receta')
        else:
            data['formu'] = formulario

    return render(request, "servicios/modificar_receta.html", data)


@login_required
def eliminar_receta(request, id):
    citas = get_object_or_404(receta_medica, id=id)
    citas.delete()
    return redirect(to="receta")  