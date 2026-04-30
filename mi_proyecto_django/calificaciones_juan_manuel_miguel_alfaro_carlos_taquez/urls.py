from django.urls import path

from .views import (
    CrearCalificacionView,
    EditarCalificacionView,
    EliminarCalificacionView,
    ListarCalificacionView,
)

urlpatterns = [
    path('', ListarCalificacionView.as_view(), name='listar'),
    path('crear/', CrearCalificacionView.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarCalificacionView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', EliminarCalificacionView.as_view(), name='eliminar'),
]
