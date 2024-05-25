
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notes.views import NotesViewSet

router = DefaultRouter()
router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
