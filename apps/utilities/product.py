"""Products models."""

# Django
from django.db import models

# Models
from apps.products.models.features import Feature


class Product(models.Model):
    """Product base model. all the products will inherit from this model"""

    name = models.CharField(max_length=60)
    manufacturer = models.CharField(max_length=60)
    sku = models.CharField(max_length=20)

    feature = models.ManyToManyField(Feature, related_name='feature')

    class Meta:
        """Meta option."""

        abstract = True