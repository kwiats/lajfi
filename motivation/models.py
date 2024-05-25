from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


# Create your models here.
class Achievement(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    points = models.IntegerField()
    conditions = models.JSONField(default=dict)

    def __str__(self):
        return self.title


class UserAchievement(BaseModel):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_earned = models.DateTimeField(auto_now_add=True)
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.achievement.title}"
