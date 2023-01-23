from django.http import HttpRequest, HttpResponse
from app.views.base_view import BaseView


class PageHomeView(BaseView):

    @staticmethod
    def view_route() -> str:
        return "/"

    @staticmethod
    def template_name() -> str:
        return ""

    async def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("")
