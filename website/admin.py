from django.contrib import admin

from .models import Comment, Favourite, Ingredient, Recipe, Step

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Favourite)
admin.site.register(Comment)
