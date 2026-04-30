from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def listar(request):
    return HttpResponse("OK - listar (pendiente implementar plantilla/CRUD)")
