import asyncio
from json import dumps

from django.template.loader import render_to_string
from django.http import HttpRequest, HttpResponse

# Create your views here.


async def index(request: HttpRequest) -> HttpResponse:
    route = request.get_full_path()
    return HttpResponse(render_to_string(
        "pages/home.html",
        {
            "loadPage1": "true" if "page-1" in route else "false",
            "loadPage2": "true" if "page-2" in route else "false",
            "loadPage3": "true" if "page-3" in route else "false"
        }))


async def page_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("")


async def page_one(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render_to_string(
        "components/name.html",
        {"name": "Beatriz"}
    ))


async def page_two(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render_to_string(
        "components/name.html",
        {"name": "Mundo"})
    )


async def page_three(request: HttpRequest) -> HttpResponse:
    return HttpResponse(render_to_string(
        "components/name.html",
        {"name": "Cruz"}))
