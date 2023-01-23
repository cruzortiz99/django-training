from django.views import View
from abc import abstractmethod


class BaseView(View):
    @staticmethod
    @abstractmethod
    def view_route() -> str:
        pass

    @staticmethod
    @abstractmethod
    def template_name() -> str:
        pass
