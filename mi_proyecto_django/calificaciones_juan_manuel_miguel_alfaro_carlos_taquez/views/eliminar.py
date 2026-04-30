from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ..models import Calificacion


class EliminarCalificacionView(LoginRequiredMixin, DeleteView):
    model = Calificacion
    template_name = 'calificaciones/eliminar.html'
    success_url = reverse_lazy('listar')
