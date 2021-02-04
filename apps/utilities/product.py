"""Products models."""

# Django
from django.db import models

# Models
from .features import Feature


class Product(models.Model):
    """Product base model. all the products will inherit from this model"""

    name = models.CharField()
    manufacturer = models.CharField()
    sku = models.CharField()

    feature = models.ManyToManyField(Feature, related_name='feature')

    class Meta:
        """Meta option."""

        abstract = True