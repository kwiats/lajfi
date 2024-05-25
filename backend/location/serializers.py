from rest_framework import serializers

from location.models import Location, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['uuid', 'name']


class LocationSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Location
        fields = ['uuid', 'user', 'name', 'description', 'latitude', 'longitude', 'tags']
