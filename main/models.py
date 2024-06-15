import uuid
from django.db import models
from custom_user.models import CustomUser

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

