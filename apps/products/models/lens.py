"""Lens models."""

# Django
from django.db import models

# Models
from apps.utilities import RandomCamerasModel
from apps.utilities.product import Product
from .features import Feature

class Lens(Product, RandomCamerasModel):
    """Lens model."""

    brand = models.CharField(max_length=20)
    lens_aperture = models.CharField(max_length=7)
    focal_distance = models.CharField(max_length=20)

    feature = models.ManyToManyField(Feature, related_name='l_feature')

    def __str__(self):
            return self.title

