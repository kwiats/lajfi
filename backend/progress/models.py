from django.db import models

from common.models import BaseModel
from task.models import Task


# Create your models here.
class Progress(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # Progress in percentage

    def __str__(self):
        return f"{self.task.title} - {self.progress}%"