from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

TEMP = (
    ('Hot', 'Hot'),
    ('Cold', 'Cold'),
)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'This is {self.name}'
    
    def get_absolute_url(self):
        return reverse("ingredients_detail", kwargs={"pk": self.pk})


class Sandwich(models.Model):
    name = models.CharField(max_length=50)
    temp = models.CharField(
        max_length=4,
        choices=TEMP,
        default=TEMP[0][1]
    )
    description = models.TextField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    







