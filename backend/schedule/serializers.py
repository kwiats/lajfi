from rest_framework import serializers

from schedule.models import Event


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Event
        fields = ['uuid', 'user', 'title', 'description', 'start_time', 'end_time', 'created_at', 'updated_at']
