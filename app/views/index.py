from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.views.base_view import BaseView


class IndexView(BaseView):
    @property
    def view_route(self) -> str:
        return "/"

    @property
    def template_name(self) -> str:
        return "pages/home.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        route = request.get_full_path()
        return render(
            request,
            self.template_name,
            {
                "login": "true" if "login" in route else "false",
                "sign_in": "true" if "sign-in" in route else "false",
                "adoption_center": "true" if "adoption-centers" in route
                else "false",
                "pet_store": "true" if "pet-stores" in route else "false",
                "user": "true" if "users" in route else "false",
            })
