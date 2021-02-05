"""Lens reviews views."""

# Rest framework
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework import status, viewsets, mixins

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from apps.reviews.permissions import IsReviewer, IsReviewOwner

# Serializers
from apps.reviews.serializers import LenReviewModelSerializer

# Models
from apps.reviews.models import LenReview

class LensReviewsViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    """Reviews view set."""

    serializer_class = LenReviewModelSerializer

    def get_permissions(self):
        """Assing permissions based on actions."""

        if self.action in ['update', 'partial_update']:
            """Only reviewers can edit reviews."""
            permissions = [IsAuthenticated, IsReviewer, IsReviewOwner]
        
        else:
            permissions = [AllowAny]

        return [p() for p in permissions]

    def get_object(self):
        return get_object_or_404(
            LenReview,
            pk=self.kwargs['pk']
        )

    def get_queryset(self):
        """Assing querys based on actions."""

        queryset = LenReview.objects.all()

        if self.action in ['update', 'partial_update', 'retrieve']:
            queryset.get(pk=self.kwargs['pk'])

        return queryset

    


