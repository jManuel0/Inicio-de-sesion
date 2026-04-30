from django.contrib import admin

from .models import Calificacion


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'asignatura', 'nota_1', 'nota_2', 'nota_3', 'promedio')
    search_fields = ('estudiante', 'asignatura')
