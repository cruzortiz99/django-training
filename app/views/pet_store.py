from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.views.base_view import BaseView


class PagePetStoreView(BaseView):
    @staticmethod
    def view_route() -> str:
        return "/pet-stores/"

    @staticmethod
    def template_name() -> str:
        return "pages/pet-store.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,
                      PagePetStoreView.template_name(),
                      {"name": "Beatriz"})
