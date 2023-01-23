from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.views.base_view import BaseView


class IndexView(BaseView):
    @staticmethod
    def view_route() -> str:
        return "/"

    @staticmethod
    def template_name() -> str:
        return "pages/home.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        route = request.get_full_path()
        return render(
            request,
            IndexView.template_name(),
            {
                "login": "true" if "login" in route else "false",
                "sign_in": "true" if "sign-in" in route else "false",
                "adoption_center": "true" if "adoption-centers" in route
                else "false",
                "pet_store": "true" if "pet-stores" in route else "false",
                "user": "true" if "users" in route else "false",
            })
