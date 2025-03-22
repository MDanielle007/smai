from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='services')  # Add basename parameter

urlpatterns = [
    path("", include(router.urls)),
]
