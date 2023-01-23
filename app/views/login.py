from app.views.base_view import BaseView
from app.views.user import PageUser
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


class PageLoginView(BaseView):

    @staticmethod
    def view_route() -> str:
        return "/login/"

    @staticmethod
    def template_name() -> str:
        return "pages/login.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, PageLoginView.template_name())

    async def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(PageUser.view_route())
