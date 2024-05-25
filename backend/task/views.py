from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from task.models import Task
from task.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        task.check_achievements()

    def perform_update(self, serializer):
        task = serializer.save()
        task.check_achievements()
