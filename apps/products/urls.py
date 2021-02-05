"""Users urls."""

# Django
from django.urls import path, include

# Rest framework
from rest_framework.routers import DefaultRouter

# views
from apps.products.views import CamerasViewSet, LensViewSet

# Router init
router = DefaultRouter()
router.register(r'cameras', CamerasViewSet, basename='camera')
router.register(r'lens', LensViewSet, basename='len')

urlpatterns = [
    path('products/', include(router.urls))
]