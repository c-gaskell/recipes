from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """Custom Signup form.

    Extends built-in form and adds name and email.
    """

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name",
                  "email", "username", "password1", "password2")
