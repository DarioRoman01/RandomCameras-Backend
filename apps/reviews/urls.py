"""Users urls."""

# Django
from django.urls import path, include

# Rest framework
from rest_framework.routers import DefaultRouter

# views
from apps.reviews.views import CamerasReviewsViewSet, LensReviewsViewSet

# Router init
router = DefaultRouter()
router.register(r'cameras', CamerasReviewsViewSet, basename='camera_r')
router.register(r'lens', LensReviewsViewSet, basename='len_r')


urlpatterns = [
    path('reviews/', include(router.urls))
]