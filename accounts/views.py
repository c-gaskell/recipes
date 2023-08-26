from django.urls import reverse_lazy
from django.views import generic

from .forms import SignUpForm

class Signup(generic.CreateView):
    """Signup Page."""

    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
