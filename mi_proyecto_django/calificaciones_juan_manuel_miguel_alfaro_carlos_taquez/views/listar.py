from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.views.generic import ListView

from ..models import Calificacion


class ListarCalificacionView(LoginRequiredMixin, ListView):
    model = Calificacion
    template_name = 'calificaciones/listar.html'
    context_object_name = 'calificaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promedio_general'] = Calificacion.objects.aggregate(
            promedio_general=Avg('promedio')
        )['promedio_general']
        return context
