from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms import CalificacionForm
from ..models import Calificacion


class CrearCalificacionView(LoginRequiredMixin, CreateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = 'calificaciones/crear.html'
    success_url = reverse_lazy('listar')
