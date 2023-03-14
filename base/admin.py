#helps to create superusers
from django.contrib import admin
from .models import Ingredient

admin.site.register(Ingredient)

# Register your models here.
