from django.views import View
from abc import abstractmethod


class BaseView(View):
    @property
    @abstractmethod
    def view_route(self) -> str:
        pass

    @property
    @abstractmethod
    def template_name(self) -> str:
        pass
