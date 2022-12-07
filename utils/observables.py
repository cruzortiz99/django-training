from typing import Callable, Coroutine, Any, TypeVar, Optional
import asyncio
import reactivex as rx
from reactivex.disposable import Disposable
T = TypeVar('T')


def from_async(
        afunc: Callable[[], Coroutine[Any, Any, T]],
        loop: Optional[asyncio.AbstractEventLoop] = None
) -> rx.observable.Observable[T]:
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


async def connect_to_observable(observable: rx.observable.Observable[T]) -> T:
    result: asyncio.Future = asyncio.Future()
    subscription = observable.subscribe(
        on_next=result.set_result,
        on_error=result.set_exception,
    )
    response = await result
    subscription.dispose()
    return response
