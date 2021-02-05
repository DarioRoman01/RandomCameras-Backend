"""Cameras models."""

# Django
from django.db import models

# Models
from apps.utilities import RandomCamerasModel
from apps.utilities.product import Product
from .features import Feature

class Camera(Product, RandomCamerasModel):
    """Camera model."""

    maxISO = models.PositiveIntegerField(default=0)
    
    tipe = models.CharField(max_length=50)

    crop_factor = models.CharField(max_length=20)

    feature = models.ManyToManyField(Feature, related_name='c_features')


    def __str__(self):
        return self.name

