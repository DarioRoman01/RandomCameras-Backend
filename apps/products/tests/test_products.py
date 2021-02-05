"""Products test."""

# Django
from django.test import TestCase

# Models
from apps.products.models import Camera
from apps.products.models.features import Feature

class ProductsTestCase(TestCase):
    """Products test case."""

    def setUp(self):
        """Test case setup."""
        self.product = Camera.objects.create(
            name='Camara Sony A68',
            manufacturer='Sony',
            sku='349857',
            maxISO='15',
            tipe='camera',
            crop_factor='DT 18-55 mm'
        )

        self.feature = Feature.objects.create(
            name='Flash',
            description='Has flash'
        )


    def test_has_content_and_feature(self):
        """Check that the objects has info and can add feature."""

        product = self.product
        feature = self.feature

        product.feature.add(feature)

        self.assertIsNotNone(product)
        self.assertIsNotNone(product.feature.all())