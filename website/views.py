from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request: HttpRequest) -> HttpResponse:
    """Basic Test Page. Used for checking templates, styles etc."""
    return render(request, "website/test.html")


def home(request: HttpRequest) -> HttpResponse:
    """Website Homepage."""
    return render(request, "website/home.html")
