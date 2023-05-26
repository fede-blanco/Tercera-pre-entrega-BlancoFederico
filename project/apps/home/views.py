from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


# "home/index.html" --> Ruta a la vista (la cual busca en la carpeta templates porque asi se configuro en settings.py)
# request --> Lo recibe siempre es una peticion http, en este caso "GET"
