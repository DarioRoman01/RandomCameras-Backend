"""reviews models."""

# Django
from django.db import models

# Models
from apps.users.models import User


class Review(models.Model):
    """Review base model. all reviews extends from this model
    to be more scalable if more products than camera or lens are
    reviewed"""

    title = models.CharField(max_length=30)
    content = models.TextField(max_length=800)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta option."""

        abstract = True