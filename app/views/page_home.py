from django.http import HttpRequest, HttpResponse
from app.views.base_view import BaseView


class PageHomeView(BaseView):

    @property
    def view_route(self) -> str:
        return "/"

    @property
    def template_name(self) -> str:
        return ""

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("")
