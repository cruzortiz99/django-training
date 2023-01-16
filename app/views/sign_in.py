from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.views.base_view import BaseView


class PageSignInView(BaseView):
    @property
    def view_route(self) -> str:
        return "/sign-in/"

    @property
    def template_name(self) -> str:
        return "pages/sign-in.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
