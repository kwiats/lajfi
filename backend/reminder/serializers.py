from rest_framework import serializers
from reminder.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Reminder
        fields = ['uuid', 'user', 'title', 'description', 'remind_at', 'created_at', 'updated_at']
