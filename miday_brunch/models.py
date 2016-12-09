from __future__ import unicode_literals

from django.db import models

class Meal(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=250)
    quantity=models.CharField(max_length=50)
