from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['uuid', 'user', 'title', 'description', 'priority', 'due_date', 'completed', 'created_at',
                  'updated_at']
