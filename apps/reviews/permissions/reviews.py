"""Reviews permissions."""

# REST Framework
from rest_framework.permissions import BasePermission

# Models
from apps.reviews.models import CameraReview

class IsReviewOwner(BasePermission):
    """Is review owner permission."""

    def has_object_permission(self, request, view, obj):
        """Check if the reviewer is the creator of the review."""
        try:
            CameraReview.objects.filter(user=request.user)

        except CameraReview.DoesNotExist:
            return False

        return True

    

class IsReviewer(BasePermission):
    """Is reviewer permission."""

    def has_permission(self, request, view):
        """Check if the requesting user is reviewer."""
        
        if request.user.is_reviewer == True:
            return True

        else:
            return False

