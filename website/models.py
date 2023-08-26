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
        return self.title + " by " + self.author.full_name


class Step(models.Model):
    """A single step within a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.TextField()


class Ingredient(models.Model):
    """A single ingredient within a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.FloatField()
    unit = models.CharField(max_length=1)  # One of m, kg, C (as in degrees celcius), or L.
    # Conversions to imperial or other units will be done elsewhere, all stored values are metric, in these 4 units.


class Favourite(models.Model):
    """Instance of a user favouriting a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    """Comment on a recipe."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
