from django.urls import path, include
from rest_framework.routers import DefaultRouter
from progress.views import ProgressViewSet

router = DefaultRouter()
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
