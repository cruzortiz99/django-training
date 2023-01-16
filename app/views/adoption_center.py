from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from app.views.base_view import BaseView


class PageAdoptionCenterView(BaseView):
    @property
    def view_route(self) -> str:
        return "/adoption-centers/"

    @property
    def template_name(self) -> str:
        return "pages/adoption-center.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"name": "Cruz"})
