from typing import Any, Dict

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Recipe


def is_author(user: User) -> bool:
    """Check if user is an author."""
    return user.groups.filter(name='Author').exists()


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

    def get(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        """HTTP GET Method.

        Generic method which will use get_page_attrs and self.template.
        If a subclass only needs custom attributes, just override get_page_attrs and not this method.
        """
        attrs = self.get_page_attrs(request)
        return render(request, self.template, attrs)


class TestView(BaseView):
    """Basic Test Page. Used for checking templates, styles etc."""

    template = "website/test.html"


class HomeView(BaseView):
    """Homepage view."""

    template = "website/home.html"

    def get_page_attrs(self, request: HttpRequest) -> Dict[str, str]:
        """Get recipies to display in page."""
        attrs = super().get_page_attrs(request)
        attrs['recipies'] = Recipe.objects.all().order_by("title")
        return attrs


class CreateView(BaseView):
    """Recipe Creation page."""

    template = "website/create.html"


class ProfileView(BaseView):
    """User's profile page."""

    template = "website/profile.html"


class RecipeView(BaseView):
    """Recipe page."""

    template = "website/recipe.html"
