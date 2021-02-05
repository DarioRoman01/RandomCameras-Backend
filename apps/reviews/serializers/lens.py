"""Lens review serializers."""

# Rest framework
from rest_framework import serializers

# Models
from apps.reviews.models import LenReview

# serializers
from apps.products.serializers import LensModelSerializer
from apps.users.serializers import UserModelSerializer

class LenReviewModelSerializer(serializers.ModelSerializer):
    """Len review model serializer."""

    product = LensModelSerializer(read_only=True)
    author = UserModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = LenReview
        fields =(
            'title',
            'content',
            'product',
            'author',
        )


class CreateLenReviewSerializer(serializers.Serializer):
    """Create len review serializer."""

    title = serializers.CharField(max_length=30)
    content = serializers.CharField(max_length=800)

    def create(self, validated_data):
        author = self.context['request'].user
        product = self.context['product']

        len_review = LenReview.objects.create(
            **validated_data,
            author=author,
            product=product
        )

        return len_review



