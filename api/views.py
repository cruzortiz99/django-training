import asyncio
from json import dumps

import reactivex.operators as rx_op

from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.


async def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


async def say_hello(request: HttpRequest) -> HttpResponse:
    return render(request, "components/name.html", {"name": "Cruz"})


async def createMessage() -> str:
    print("waiting")
    await asyncio.sleep(1)
    return "Hola"


def addMundo(start: str) -> str:
    return f"{start} Mundo"


def createHttpResponse(message: str) -> HttpResponse:
    return HttpResponse(
        content=dumps({"message": message}),
        content_type="application/json"
    )
