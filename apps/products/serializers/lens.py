"""Lens serializers."""

# Rest framework
from rest_framework import serializers

# Models
from apps.products.models import Lens
from apps.products.models.features import Feature

# Serializers
from .features import FeatureModelSerializer

class LensModelSerializer(serializers.ModelSerializer):
    """Lens model serializer."""

    feature = FeatureModelSerializer(read_only=True, many=True)

    class Meta:
        """Meta class."""

        model = Lens
        fields = (
            'name',
            'manufacturer',
            'sku',
            'brand',
            'lens_aperture',
            'focal_distance',
            'feature',
        )


class CreateLenSerializer(serializers.Serializer):
    """Create lens product serializer."""

    name = serializers.CharField(max_length=60)
    manufacturer = serializers.CharField(max_length=60)
    sku = serializers.CharField(max_length=20)
    brand = serializers.CharField(max_length=20)
    lens_aperture = serializers.CharField(max_length=7)
    focal_distance = serializers.CharField(max_length=20)

    def create(self, validated_data):
        
        lens = Lens.objects.create(**validated_data)

        return lens


class AddLenFeatureSerializer(serializers.Serializer):
    """Add feature serializer."""

    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """Create Feature and added to the product that 
        come from the context."""

        feature = Feature.objects.create(**validated_data)

        lens = self.context['len']

        lens.feature.add(feature)

        return lens