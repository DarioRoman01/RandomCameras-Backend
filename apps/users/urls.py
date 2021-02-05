"""Users urls."""

# Django
from django.urls import path, include

# Rest framework
from rest_framework.routers import DefaultRouter

# views
from apps.users import views

# Router init
router = DefaultRouter()
router.register(r'users', views.UsersViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]