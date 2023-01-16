from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from typing import Final
from app.views.user import PageUser


class PageLoginView(View):
    view_route: Final = "/login/"
    template_name: Final = "pages/login.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

    async def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(PageUser.view_route)
