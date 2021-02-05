"""Products permissions."""

# Rest Framework
from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    """Is staff permissions. only staff can create
    new products."""

    def has_permission(self, request, view):
        """Check that the user is staff."""
        
        if request.user.is_staff:
            return True

        else:
            return False