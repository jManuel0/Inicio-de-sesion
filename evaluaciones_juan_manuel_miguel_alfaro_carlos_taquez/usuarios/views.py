from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import RegistroForm


@require_http_methods(["GET", "POST"])
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("calificaciones:listar")
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})
