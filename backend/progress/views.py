from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from progress.models import Progress
from progress.serializers import ProgressSerializer
from task.models import Task


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task_id = self.request.data.get('task_id')
        task = Task.objects.get(id=task_id)
        serializer.save(task=task)
