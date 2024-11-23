from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.IntegerField(primary_key=True, unique=True,blank=False, null=False)
    name = models.TextField(max_length=64, blank=False, null=False)
    item_code = models.IntegerField(blank=False, null=False)
    description = models.TextField(max_length=256)
    price = models.DecimalField(blank=False, null=False, max_digits=16, decimal_places=2)