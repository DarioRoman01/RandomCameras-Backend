"""Products views."""

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
    CameraModelSerializer,
    CreateCameraSerializer,
    AddCameraFeatureSerializer
)

from apps.reviews.serializers import (
    CreateCameraReviewSerializer,
    CameraReviewModelSerializer
)

# Models
from apps.products.models import Camera


class CamerasViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    """camera view set."""

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
            Camera,
            pk=self.kwargs['pk']
        )

    def get_queryset(self):
        """Assing querys based on actions."""

        queryset = Camera.objects.all()

        if self.action in ['update', 'partial_update', 'retrieve', 
                           'review', 'addfeature']:

            """All the actions is for one specific product."""
            queryset.get(pk=self.kwargs['pk'])
            
        return queryset

    @action(detail=False, methods=['POST'])
    def store(self, request):
        """Handle products creation."""

        serializer = CreateCameraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        camera = serializer.save()

        data = CameraModelSerializer(camera).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def review(self, request, pk):
        """Handle reviews creation."""

        product = self.get_object()

        serializer = CreateCameraReviewSerializer(
            context={'request': request, 'product': product},
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        camera_review = serializer.save()
        data = CameraReviewModelSerializer(camera_review).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def addfeature(self, request, pk):
        """Handle add features to cameras."""

        product = self.get_object()
        serializer = AddCameraFeatureSerializer(
            context={'camera': product},
            data=request.data
        )
        serializer.is_valid()
        camera = serializer.save()

        data = CameraModelSerializer(camera).data

        return Response(data, status=status.HTTP_201_CREATED)

        



    