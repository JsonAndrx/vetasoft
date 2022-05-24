from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import pacientes, mascota_sexo, tipo_mascota, propietario, tipo_documento, veterinario
from .forms import FormularioPacientes, FormularioPropietario, FormularioVeterinario

 
# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})


@login_required
def pacientesv(request):
    data = {
        'paciente':pacientes.objects.all(),
        'formu':FormularioPacientes(),
        'mensaje':'OK'}
    if request.method == 'POST':
        formulario = FormularioPacientes(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registro exitoso"
        else:
            data["formu"]=formulario

    return render(request, "registration/pacientes.html", data)


@login_required
def modificar_paciente(request, id):
    paciente = get_object_or_404(pacientes,id=id)
    data = {'formu': FormularioPacientes(instance=paciente)}

    if request.method == 'POST':
        formulario = FormularioPacientes(data=request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pacientes")
        else:
            data['formu'] = formulario
        
    return render(request, "registration/modificar.html", data)


@login_required
def eliminar_paciente(request, id):
    paciente = get_object_or_404(pacientes,id=id)
    paciente.delete()
    return redirect(to="pacientes")


@login_required
def propietarios(request):
    data = {
        'propietario': propietario.objects.all(),
        'formu': FormularioPropietario(),
        'mensaje':"OK" }
    if request.method == 'POST':
        formulario = FormularioPropietario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Registro exitoso"
        else:
            data["formu"]=formulario

    return render(request, 'registration/propietario.html', data)

@login_required
def modificar_propietario(request, id):
    propietarios = get_object_or_404(propietario, id=id)
    data = {"formu":FormularioPropietario(instance=propietarios)}

    if request.method == 'POST':
        formulario = FormularioPropietario(data=request.POST, instance=propietarios)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="propietario")
        else:
            data["formu"]=formulario
    
    return render(request, "registration/modificar_propietario.html", data)


@login_required
def eliminar_propietario(request, id):
    propietarios =get_object_or_404(propietario, id=id)
    propietarios.delete()
    return redirect(to='propietario')


@login_required
def veterinarios(request):
    data = {
        'veterinario': veterinario.objects.all(),
        'formu': FormularioVeterinario(),
        'mensaje': 'OK'}
    if request.method == 'POST':
        formulario = FormularioVeterinario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registro exitoso"
        else:
            data['formu']=formulario
        
    return render(request, "registration/veterinario.html", data)


@login_required
def modificar_veterinario(request, id):
    veterinarios = get_object_or_404(veterinario, id=id)
    data = {'formu': FormularioVeterinario(instance=veterinarios)}
    
    if request.method == 'POST':
        formulario = FormularioVeterinario(data=request.POST, instance=veterinarios)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="veterinarios")
        else:
            data["formu"]=formulario

    return render(request, "registration/modificar_veterinario.html", data)


@login_required
def eliminar_veterinario(request, id):
    veterinarios = get_object_or_404(veterinario, id=id)
    veterinarios.delete()
    return redirect(to='veterinarios')




