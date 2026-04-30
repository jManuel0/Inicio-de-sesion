from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from ..forms import CalificacionForm
from ..models import Calificacion


class EditarCalificacionView(LoginRequiredMixin, UpdateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = 'calificaciones/editar.html'
    success_url = reverse_lazy('listar')
