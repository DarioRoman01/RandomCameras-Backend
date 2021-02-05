"""Cameras serializers."""

# Rest framework
from rest_framework import serializers

# Models
from apps.products.models import Camera
from apps.products.models.features import Feature

# Serializers
from .features import FeatureModelSerializer


class CameraModelSerializer(serializers.ModelSerializer):
    """Camera model serializer."""

    feature = FeatureModelSerializer(read_only=True, many=True)

    class Meta:
        """Meta class."""

        model = Camera

        fields = (
            'name',
            'manufacturer',
            'sku',
            'maxISO',
            'tipe',
            'crop_factor',
            'feature'
        )

class CreateCameraSerializer(serializers.Serializer):
    """Create camera product serializer."""

    name = serializers.CharField(max_length=60)
    manufacturer = serializers.CharField(max_length=60)
    sku = serializers.CharField(max_length=20)
    maxISO = serializers.IntegerField()
    tipe = serializers.CharField(max_length=50)
    crop_factor = serializers.CharField(max_length=20)

    def create(self, validated_data):
        """Handle products creation."""

        camera = Camera.objects.create(**validated_data)

        return camera

class AddCameraFeatureSerializer(serializers.Serializer):
    """Add feature serializer."""

    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """Create Feature and added to the product that 
        come from the context."""

        feature = Feature.objects.create(**validated_data)

        camera = self.context['camera']

        camera.feature.add(feature)

        return camera

