from rest_framework import serializers
from progress.models import Progress
from task.serializers import TaskSerializer


class ProgressSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)

    class Meta:
        model = Progress
        fields = ['uuid', 'task', 'progress', 'created_at', 'updated_at']
