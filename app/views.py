from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from django.views import View

# Create your views here.


class IndexView(View):
    async def get(self, request: HttpRequest) -> HttpResponse:
        route = request.get_full_path()
        return HttpResponse(render_to_string(
            "pages/home.html",
            {
                "loadPage1": "true" if "page-1" in route else "false",
                "loadPage2": "true" if "page-2" in route else "false",
                "loadPage3": "true" if "page-3" in route else "false"
            }))


class PageHomeView(View):
    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("")


class PageOneView(View):
    template_name = "components/name.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(render_to_string(
            self.template_name,
            {"name": "Beatriz"}
        ))


class PageTwoView(View):
    template_name = "components/name.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(render_to_string(
            self.template_name,
            {"name": "Mundo"})
        )


class PageThree(View):
    template_name = "components/name.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(render_to_string(
            self.template_name,
            {"name": "Cruz"}))
