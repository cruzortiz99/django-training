from django.http import HttpResponse, HttpRequest
# Create your views here.


def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse("Hola Mundo")
