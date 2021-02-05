"""Camera reviews serializers."""

# Rest framework
from rest_framework import serializers

# Models
from apps.reviews.models import CameraReview
from apps.products.models import Camera

# Serializers
from apps.products.serializers import CameraModelSerializer
from apps.users.serializers import UserModelSerializer

class CameraReviewModelSerializer(serializers.ModelSerializer):
    """Camera review model serializer."""

    product = CameraModelSerializer(read_only=True)
    author = UserModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = CameraReview
        fields =(
            'title',
            'content',
            'product',
            'author',
        )


class CreateCameraReviewSerializer(serializers.Serializer):
    """Create camera review serializer."""

    title = serializers.CharField(max_length=30)
    content = serializers.CharField(max_length=800)

    def create(self, validated_data):
        author = self.context['request'].user
        product = self.context['product']

        camera_review = CameraReview.objects.create(
            **validated_data,
            author=author,
            product=product
        )

        return camera_review
