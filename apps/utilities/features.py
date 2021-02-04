"""Features models."""

# Django
from django.db import models

class Feature(models.Model):
    """Feature model."""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name