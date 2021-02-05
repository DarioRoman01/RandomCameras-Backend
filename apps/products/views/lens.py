"""Lens views."""

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
from apps.products.permissions import IsStaff
from apps.reviews.permissions import IsReviewer

# Serializers
from apps.products.serializers import (
    LensModelSerializer,
    CreateLenSerializer,
    AddLenFeatureSerializer
)

from apps.reviews.serializers import (
    CreateLenReviewSerializer,
    LenReviewModelSerializer
)

# Models
from apps.products.models import Lens

class LensViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    """Lens view set."""

    def get_permissions(self):
        """Assing permissions based on actions."""
        if self.action in ['update', 'partial_update', 'store', 'addfeature']:
            """Only staff can add or modified products."""
            permissions = [IsAuthenticated, IsStaff]

        elif self.action in ['review']:
            permissions = [IsAuthenticated, IsReviewer]

        else:
            permissions = [AllowAny]

        return [p() for p in permissions]

    def get_object(self):
        """Get specific post."""

        return get_object_or_404(
            Lens,
            pk=self.kwargs['pk']
        )

    def get_queryset(self):
        """Assing querys based on actions."""

        queryset = Lens.objects.all()

        if self.action in ['update', 'partial_update', 'retrieve', 
                           'review', 'addfeature']:

            """All the actions is for one specific product."""
            queryset.get(pk=self.kwargs['pk'])

        return queryset

    @action(detail=False, methods=['POST'])
    def store(self, request):
        """Handle lens creation."""

        serializer = CreateLenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lens = serializer.save()

        data = LensModelSerializer(lens).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def review(self, request, pk):
        """Handle lens review creation."""

        product = self.get_object()
        serializer = CreateLenReviewSerializer(
            context={'request': request, 'product': product},
            data=request.data
        )
        serializer.is_valid()
        len_review = serializer.save()
        data = LenReviewModelSerializer(len_review).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def addfeature(self, request, pk):
        """Handle add features to cameras."""

        product = self.get_object()
        serializer = AddLenFeatureSerializer(
            context={'len': product},
            data=request.data
        )
        serializer.is_valid()
        lens = serializer.save()

        data = LensModelSerializer(lens).data

        return Response(data, status=status.HTTP_201_CREATED)
