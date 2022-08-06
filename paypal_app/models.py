from django.db import models

# Create your models here.
class Order(models.Model):
    paid=models.BooleanField(default=False)