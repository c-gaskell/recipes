from django.conf import settings
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    """Model representing a single recipe.

    Steps and Ingredients are separate models and contain foreign keys to the recipe.
    """

    class Meta:
        ordering = ["author", "title"]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title + " by " + self.author.get_full_name()


class Step(models.Model):
    """A single step within a recipe."""

    class Meta:
        ordering = ["recipe", "number"]

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

    class Meta:
        ordering = ["unit", "amount"]

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
        return self.human_readable() + " " + self.name + " in <" + str(self.recipe) + ">"

    def human_readable(self, imperial: bool = False) -> str:
        """Return human-readable form of amount and unit."""
        if self.amount < 1.0 and self.LESSER_UNITS[self.unit]:
            return f"{self.amount * 1000:.0f}{self.LESSER_UNITS[self.unit]}"
        else:
            return f"{self.amount:.0f}{self.READABLE_UNITS[self.unit]}"


class Favourite(models.Model):
    """Instance of a user favouriting a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    """Comment on a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
