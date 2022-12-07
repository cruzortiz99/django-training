import asyncio
from json import dumps

import reactivex.operators as rx_op

from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from utils.observables import connect_to_observable, from_async

# Create your views here.


async def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render_to_string("hello.html", {"name": "Cruz"}))


async def say_hello(request: HttpRequest) -> HttpResponse:
    response = await connect_to_observable(
        from_async(createMessage, asyncio.get_event_loop()).pipe(
            rx_op.map(addMundo),
            rx_op.map(createHttpResponse),
        ))
    return response


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
