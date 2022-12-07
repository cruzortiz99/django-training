from django.http import HttpRequest, HttpResponse
from json import dumps
from django.template.loader import render_to_string
import reactivex as rx
import reactivex.operators as rx_op
import asyncio
from typing import Callable, Any, Coroutine, TypeVar, Optional
# Create your views here.


async def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render_to_string("hello.html", {"name": "Cruz"}))


def say_hello(request: HttpRequest) -> HttpResponse:
    return from_async(createMessage).pipe(
        rx_op.map(addMundo),
        rx_op.map(createHttpResponse),
    ).run()


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


T = TypeVar("T")


def from_async(
        afunc: Callable[[], Coroutine[Any, Any, T]],
        loop: Optional[asyncio.AbstractEventLoop] = None):
    def producer(
            observer: rx.abc.ObserverBase,
            scheduler: Optional[rx.abc.SchedulerBase]
    ):
        async def fetch_result() -> None:
            try:
                observer.on_next(await afunc())
                observer.on_completed()
            except Exception as error:
                observer.on_error(error)
        asyncio.run(fetch_result())
    return rx.create(producer)
