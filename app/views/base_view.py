from django.views import View


class BaseView(View):
    def view_route(self) -> str:
        raise Exception("Must override method")

    def template_name(self) -> str:
        raise Exception("Must override method")
