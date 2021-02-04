"""Reviews models."""

# Django
from django.db import models

# Models
from apps.utilities import RandomCamerasModel
from apps.users.models import User
from apps.products.models import Camera

class Review(RandomCamerasModel):
    """Review model."""

    title = models.CharField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Camera, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
