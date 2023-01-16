from django.views import View
from django.http import HttpRequest, HttpResponse
from typing import Final


class PageHomeView(View):
    view_route: Final = "/"

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("")
