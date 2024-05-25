from django.urls import path, include
from rest_framework.routers import DefaultRouter

from location.views import LocationViewSet, TagViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
