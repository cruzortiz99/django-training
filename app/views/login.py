from app.views.base_view import BaseView
from app.views.user import PageUser
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


class PageLoginView(BaseView):

    @property
    def view_route(self) -> str:
        return "/login/"

    @property
    def template_name(self) -> str:
        return "pages/login.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

    async def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(PageUser.view_route)
