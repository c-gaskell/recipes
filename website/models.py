from django.conf import settings
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    """Model representing a single recipe.

    Steps and Ingredients are separate models and contain foreign keys to the recipe.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title + " by " + self.author.get_full_name()


class Step(models.Model):
    """A single step within a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.TextField()

    def __str__(self) -> str:
        return "Step " + str(self.number) + " in <" + str(self.recipe) + ">"


class Ingredient(models.Model):
    """A single ingredient within a recipe."""

    CHOICES = [("kg", "kg"), ("L", "L"), ("C", "°C"), ("m", "m"), ("no", "amount")]
    READABLE_UNITS = {
        "kg": "kg",
        "L": "L",
        "C": "°C",
        "m": "m",
        "no": "",
    }
    LESSER_UNITS = {
        "kg": "g",
        "L": "mL",
        "C": False,
        "m": "mm",
        "no": False,
    }

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    unit = models.CharField(
        max_length=2,
        choices=CHOICES
    )
    # One of m, kg, C (as in degrees celcius), L, or no (as in number - ie no unit).
    # Conversions to imperial or other units will be done elsewhere, all stored values are metric, in these 4 units.

    def __str__(self) -> str:
        return str(self.amount) + self.unit + " of " + self.name + " in <" + str(self.recipe) + ">"


class Favourite(models.Model):
    """Instance of a user favouriting a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    """Comment on a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
