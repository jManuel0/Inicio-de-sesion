from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CalificacionForm
from .models import Calificacion


@login_required
def listar(request):
    calificaciones = Calificacion.objects.all().order_by('nombre_estudiante', 'asignatura')
    promedio_general = calificaciones.aggregate(promedio=Avg('promedio'))['promedio']

    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general,
        'tiene_calificaciones': calificaciones.exists(),
    })


@login_required
def crear(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calificacion creada correctamente.')
            return redirect('calificaciones:listar')
    else:
        form = CalificacionForm()

    return render(request, 'calificaciones/crear.html', {'form': form})


@login_required
def editar(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)

    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Calificacion actualizada correctamente.')
            return redirect('calificaciones:listar')
    else:
        form = CalificacionForm(instance=calificacion)

    return render(request, 'calificaciones/editar.html', {
        'form': form,
        'calificacion': calificacion,
    })


@login_required
def eliminar(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)

    if request.method == 'POST':
        calificacion.delete()
        messages.success(request, 'Calificacion eliminada correctamente.')
        return redirect('calificaciones:listar')

    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})


@login_required
def promedio_general(request):
    return listar(request)
