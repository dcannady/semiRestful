from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def update(self, product_id, post):
        change = Products.objects.get(id=product_id)
        change.name = post['name']
        change.description = post['description']
        change.price = post['price']
        change.save()

class Products(models.Model):
        name = models.CharField(max_length=100)
        description = models.CharField(max_length=100)
        price = models.CharField(max_length=10)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        objects = ProductManager()
