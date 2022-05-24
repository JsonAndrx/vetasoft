from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import vacunas, medicina, inventario
from .forms import FormularioVacunas, FormularioMedicina, FormularioInventario
# Create your views here.

@login_required
def inventariosv(request):
    data={
        'inventarios': inventario.objects.all(),
        'formu':FormularioInventario(),
        'mensaje':'OK'}

    if request.method == 'POST':
        formulario = FormularioInventario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Registro exitoso"
        else:
            data['formu']=formulario
    
    return render(request, 'inventariado/inventarios.html', data)


@login_required
def modificar_inventario(request, id):
    inventarios = get_object_or_404(inventario, id=id)
    data = {'formu': FormularioInventario(instance=inventarios)}

    if request.method == 'POST':
        formulario = FormularioInventario(data=request.POST, instance=inventarios)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="inventarios")
        else:
            data['formu']= formulario
    
    return render(request, 'inventariado/modificar_inventario.html', data)


@login_required
def eliminar_inventario(request, id):
    inventarios = get_object_or_404(inventario, id=id)
    inventarios.delete()
    return redirect(to="inventarios")


@login_required
def medicinav(request):
    data = {
        'medicina':medicina.objects.all(),
        'formu':FormularioMedicina(),
        'mensaje':'Ok'}

    if request.method == 'POST':
        formulario = FormularioMedicina(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Registro exitoso"
        else:
            data['formu'] = formulario

    return render(request, 'inventariado/medicinas.html', data)


@login_required
def modificar_medicina(request, id):
    medicinas = get_object_or_404(medicina, id=id)
    data = {'formu': FormularioMedicina(instance=medicinas)}

    if request.method == 'POST':
        formulario = FormularioMedicina(data=request.POST, instance=medicinas)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="medicina")
        else:
            data['formu'] = formulario

    return render(request, "inventariado/modificar_medicina.html", data)


@login_required
def eliminar_medicina(request, id):
    medicinas = get_object_or_404(medicina, id=id)
    medicinas.delete()
    return redirect(to="medicina")


@login_required
def vacunasv(request):
    data = {
        'vacuna':vacunas.objects.all(),
        'formu':FormularioVacunas(),
        'mensaje':'OK'}

    if request.method == 'POST':
        formulario = FormularioVacunas(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Registro exitoso"
        else:
            data["formu"] = formulario

    return render(request, 'inventariado/vacunas.html', data)


@login_required
def modificar_vacuna(request, id):
    vacuna = get_object_or_404(vacunas, id=id)
    data = {'formu': FormularioVacunas(instance=vacuna)}

    if request.method == 'POST':
        formulario = FormularioVacunas(data=request.POST, instance=vacuna)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='vacunas')
        else:
            data['formu'] = formulario

    return render(request, "inventariado/modificar_vacunas.html", data)


@login_required
def eliminar_vacuna(request, id):
    vacuna = get_object_or_404(vacunas, id=id)
    vacuna.delete()
    return redirect(to="vacunas")