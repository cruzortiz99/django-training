from django.views import View
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from typing import Final


class PageAdoptionCenterView(View):
    view_route: Final = "/adoption-center/"
    template_name: Final = "pages/adoption-center.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"name": "Cruz"})
