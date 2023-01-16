from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from typing import Final


class IndexView(View):
    view_route: Final = "/"
    template_name: Final = "pages/home.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        route = request.get_full_path()
        return render(
            request,
            self.template_name,
            {
                "login": "true" if "login" in route else "false",
                "sign_in": "true" if "sign-in" in route else "false",
                "adoption_center": "true" if "adoption-center" in route
                else "false",
                "pet_store": "true" if "pet-store" in route else "false",
                "user": "true" if "user" in route else "false",
            })
