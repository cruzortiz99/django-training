from typing import Callable, Coroutine, Any, TypeVar, Optional
import asyncio
import reactivex as rx
from reactivex.disposable import Disposable
T = TypeVar('T')


def from_async(
        afunc: Callable[[], Coroutine[Any, Any, T]],
        loop: Optional[asyncio.AbstractEventLoop] = None
) -> rx.observable.Observable[T]:
    if loop is None:
        return from_async_with_no_event_loop(afunc)
    return from_async_with_event_loop(afunc, loop)


def from_async_with_no_event_loop(
    afunc: Callable[[], Coroutine[Any, Any, T]]
) -> rx.observable.Observable[T]:
    def _producer(
            observer: rx.abc.ObserverBase,
            scheduler: Optional[rx.abc.SchedulerBase]
    ) -> Disposable:
        async def _fetch_result():
            try:
                observer.on_next(await afunc())
                observer.on_completed()
            except Exception as error:
                observer.on_error(error)
        asyncio.run(_fetch_result())
        return Disposable()
    return rx.create(_producer)


def from_async_with_event_loop(
    afunc: Callable[[], Coroutine[Any, Any, T]],
    loop: asyncio.AbstractEventLoop
) -> rx.observable.Observable[T]:
    def _producer(
        observer: rx.abc.ObserverBase,
        scheduler: Optional[rx.abc.SchedulerBase]
    ) -> Disposable:
        async def _fetch_result():
            try:
                observer.on_next(await afunc())
                loop.call_soon(observer.on_completed)
            except Exception as error:
                def _on_error():
                    nonlocal error
                    observer.on_error(error)
                loop.call_soon(_on_error)
        task = loop.create_task(_fetch_result())

        def _on_cancel():
            nonlocal task
            task.cancel()
        return Disposable(_on_cancel)
    return rx.create(_producer)


async def connect_to_observable(observable: rx.observable.Observable[T]) -> T:
    result: asyncio.Future = asyncio.Future()
    subscription = observable.subscribe(
        on_next=result.set_result,
        on_error=result.set_exception,
    )
    response = await result
    subscription.dispose()
    return response
