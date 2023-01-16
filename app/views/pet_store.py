from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from typing import Final


class PagePetStoreView(View):
    view_route: Final = "/pet-store/"
    template_name: Final = "pages/pet-store.html"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"name": "Beatriz"})
