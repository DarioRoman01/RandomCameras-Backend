"""Cameras models."""

# Django
from django.db import models

# Models
from apps.utilities import Product, RandomCamerasModel

class Camera(Product, RandomCamerasModel):
    """Camera model."""

    maxISO = models.PositiveIntegerField(defaut=0)
    
    type_ = models.CharField()

    crop_factor = models.CharField()

    def __str__(self):
        return self.name

