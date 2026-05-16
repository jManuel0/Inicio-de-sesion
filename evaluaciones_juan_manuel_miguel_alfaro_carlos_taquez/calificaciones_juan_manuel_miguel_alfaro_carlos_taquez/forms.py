from django import forms

from .models import Calificacion


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        exclude = ('promedio',)
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo',
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numero de identificacion',
            }),
            'asignatura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asignatura',
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '5',
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '5',
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'max': '5',
            }),
        }
