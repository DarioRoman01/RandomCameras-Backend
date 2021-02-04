"""Normal users profiles."""

# Django
from django.db import models

# Models
from apps.users.models import User
from apps.utilities import RandomCamerasModel

class Profile(RandomCamerasModel):
    """Normal users profile model. holds users public information."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile image',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

    

