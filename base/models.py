from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#creates a SQL database in Django

class Ingredient(models.Model):
    #delete ingredients if user deleted--cascade
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    ingredientname = models.CharField(max_length=200, null = True, blank = True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    #returns ingredient name when called so users can access and view ingredients
    def __str__(self):
        return self.ingredientname

    