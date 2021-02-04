"""reviewers models."""

# Django
from django.db import models

# Models
from apps.users.models import User
from apps.utilities import RandomCamerasModel

class ReviewerProfile(RandomCamerasModel):
    """Reviewers profiles models."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile image',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    about = models.CharField(max_length=255, blank=True)

    # Stats
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username