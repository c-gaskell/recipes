from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Recipe


def is_author(user: settings.AUTH_USER_MODEL) -> bool:
    """Check if user is an author."""
    return user.groups.filter(name='Author').exists()


# Create your views here.
def test(request: HttpRequest) -> HttpResponse:
    """Basic Test Page. Used for checking templates, styles etc."""
    return render(request, "website/test.html")


def home(request: HttpRequest) -> HttpResponse:
    """Website Homepage."""
    recipes = Recipe.objects.all().order_by("title")
    print(f"{request.user.username} {'is' if is_author(request.user) else 'isnt'} an author.")
    return render(request, "website/home.html", {"recipes": recipes, "author": is_author(request.user)})


def create(request: HttpRequest) -> HttpResponse:
    """Recipe Creation page."""
    return render(request, "website/create.html")


def profile(request: HttpRequest, user: str) -> HttpResponse:
    """User's profile page."""
    return render(request, "website/profile.html")


def recipe(request: HttpRequest, user: str, title: str) -> HttpResponse:
    """Recipe page."""
    return render(request, "website/recipe.html")
