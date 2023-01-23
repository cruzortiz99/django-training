from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from app.views.base_view import BaseView


class PageUser(BaseView):
    @staticmethod
    def view_route() -> str:
        return "/users/"

    @staticmethod
    def template_name() -> str:
        return "pages/user.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, PageUser.template_name(), {"name": "Mundo"})
