from rest_framework import serializers

from shopping.models import ShoppingList, ShoppingItem


class ShoppingItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ShoppingItem
        fields = ['uuid', 'user', 'name', 'quantity', 'purchased', 'created_at', 'updated_at']


class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingItemSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ShoppingList
        fields = ['uuid', 'name', 'items', 'user', 'created_at', 'updated_at']
