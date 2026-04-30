from django import forms

from .models import Calificacion


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'asignatura', 'nota_1', 'nota_2', 'nota_3']
