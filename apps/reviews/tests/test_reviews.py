"""Reviews tests."""

# Django
from django.test import TestCase

# Models
from apps.users.models import User
from apps.products.models import Camera
from apps.reviews.models import CameraReview

class ReviewsTestCase(TestCase):
    """Reviews test case."""

    def setUp(self):
        """Test case setup."""

        self.user = User.objects.create(
            first_name='Pablo',
            last_name='Trinidad',
            email='p@mlh.io',
            username='pablotrinidad',
            password='admin12345',
            is_reviewer=True
        )

        self.product = Camera.objects.create(
            name='Camara Sony A68',
            manufacturer='Sony',
            sku='349857',
            maxISO='15',
            tipe='camera',
            crop_factor='DT 18-55 mm'
        )

        user = self.user
        product = self.product

        self.review = CameraReview.objects.create(
            title='Camara Sony A68 review',
            content='is a great camera',
            author=user,
            product=product
        )


    def test_create_review(self):
        """Test review creation."""
        
        review = self.review

        self.assertIsNotNone(review)

    def test_has_author_and_product(self):
        """Check that the review has user author and product."""

        review = self.review

        self.assertIsNotNone(review.author)
        self.assertIsNotNone(review.product)


