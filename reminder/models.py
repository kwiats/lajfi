from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


# Create your models here.
class Reminder(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    remind_at = models.DateTimeField()

    def __str__(self):
        return self.title