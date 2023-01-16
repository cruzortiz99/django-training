from django.views import View
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from typing import Final


class PageUser(View):
    view_route: Final = "/user/"
    template_name: Final = "pages/user.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"name": "Mundo"})
