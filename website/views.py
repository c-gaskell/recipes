from typing import Any, Dict

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Recipe


class BaseView(View):
    """Parent class for pages using the `website/base.html` template."""

    template = "website/base.html"

    def get_page_attrs(self, request: HttpRequest) -> Dict[str, Any]:
        """Get attributes shown in the page template.

        This method will provide attributes used by the base template.
        If a subclass needs to provide its own attributes, it should also call the super function.
        """
        attrs = {}
        attrs['author'] = is_author(request.user)
        return attrs

    def get(self, request: HttpRequest) -> HttpResponse:
        """HTTP GET Method.

        Generic method which will use get_page_attrs and self.template.
        If a subclass only needs custom attributes, just override get_page_attrs and not this method.
        """
        attrs = self.get_page_attrs(request)
        return render(request, self.template, attrs)


def is_author(user: User) -> bool:
    """Check if user is an author."""
    return user.groups.filter(name='Author').exists()


# Create your views here.
def test(request: HttpRequest) -> HttpResponse:
    """Basic Test Page. Used for checking templates, styles etc."""
    return render(request, "website/test.html")


class HomeView(BaseView):
    """Homepage view."""

    template = "website/home.html"

    def get_page_attrs(self, request: HttpRequest) -> Dict[str, str]:
        """Get recipies to display in page."""
        attrs = super().get_page_attrs(request)
        attrs['recipies'] = Recipe.objects.all().order_by("title")
        return attrs


def create(request: HttpRequest) -> HttpResponse:
    """Recipe Creation page."""
    return render(request, "website/create.html")


def profile(request: HttpRequest, user: str) -> HttpResponse:
    """User's profile page."""
    return render(request, "website/profile.html")


def recipe(request: HttpRequest, user: str, title: str) -> HttpResponse:
    """Recipe page."""
    return render(request, "website/recipe.html")
