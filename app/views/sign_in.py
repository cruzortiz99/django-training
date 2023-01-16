from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from typing import Final


class PageSignInView(View):
    view_route: Final = "/sign-in/"
    template_name: Final = "pages/sign-in.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
