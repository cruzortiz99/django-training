from django.http import HttpRequest, HttpResponse
from json import dumps
from django.template.loader import render_to_string
import reactivex as rx
import reactivex.operators as rx_op
from reactivex.disposable import Disposable
import asyncio
from typing import Callable, Any, Coroutine, TypeVar, Optional
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


T = TypeVar("T")


async def connect_to_observable(observable: rx.abc.ObservableBase):
    result: asyncio.Future = asyncio.Future()
    subscription = observable.subscribe(
        on_next=result.set_result,
        on_error=result.set_result,
    )
    response = await result
    subscription.dispose()
    return response


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
                if loop is None:
                    observer.on_completed()
                else:
                    loop.call_soon(observer.on_completed)
            except Exception as error:
                if loop is None:
                    observer.on_error(error)
                else:
                    def _on_error():
                        nonlocal error
                        observer.on_error(error)
                    loop.call_soon(_on_error)
        if loop is None:
            asyncio.run(fetch_result())
            return Disposable()
        task = asyncio.ensure_future(fetch_result())

        def _on_cancel():
            nonlocal task
            task.cancel()
        return Disposable(_on_cancel)
    return rx.create(producer)
