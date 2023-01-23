from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.views.base_view import BaseView


class PageSignInView(BaseView):
    @staticmethod
    def view_route() -> str:
        return "/sign-in/"

    @staticmethod
    def template_name() -> str:
        return "pages/sign-in.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, PageSignInView.template_name())
