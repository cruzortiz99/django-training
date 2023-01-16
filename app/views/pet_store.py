from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.views.base_view import BaseView


class PagePetStoreView(BaseView):
    @property
    def view_route(self) -> str:
        return "/pet-stores/"

    @property
    def template_name(self) -> str:
        return "pages/pet-store.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"name": "Beatriz"})
