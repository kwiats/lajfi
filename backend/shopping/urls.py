from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shopping.views import ShoppingListViewSet, ShoppingItemViewSet

router = DefaultRouter()
router.register(r'shopping-lists', ShoppingListViewSet)
router.register(r'shopping-items', ShoppingItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
