from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from app.views.base_view import BaseView


class PageAdoptionCenterView(BaseView):
    @staticmethod
    def view_route() -> str:
        return "/adoption-centers/"

    @staticmethod
    def template_name() -> str:
        return "pages/adoption-center.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      PageAdoptionCenterView.template_name(),
                      {"name": "Cruz"})
