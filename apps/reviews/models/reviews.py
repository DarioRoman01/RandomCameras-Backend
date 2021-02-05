"""Reviews models."""

# Django
from django.db import models

# Models
from apps.utilities import RandomCamerasModel
from apps.utilities.reviews import Review
from apps.products.models import Camera, Lens

class CameraReview(RandomCamerasModel, Review):
    """Camera review model."""

    product = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class LenReview(RandomCamerasModel, Review):
    """Len review model."""
    
    product = models.ForeignKey(Lens, on_delete=models.CASCADE)

    def __str__(self):
        return self.title