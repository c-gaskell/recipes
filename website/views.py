from django.shortcuts import render


# Create your views here.
def test(request):
    return render(request, "website/test.html")


def home(request):
    return render(request, "website/home.html")
