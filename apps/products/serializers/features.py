"""Feature serializers."""

# Rest framework
from rest_framework import serializers

# Models
from apps.products.models.features import Feature

class FeatureModelSerializer(serializers.ModelSerializer):
    """Feature model serializer."""

    class Meta:
        """Meta class."""

        model = Feature
        fields = (
            'name',
            'description'
        )