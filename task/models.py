from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel
from motivation.achievement_checkers import task_completion, streak, time_based, day_of_week, holiday, collaborative, \
    priority, category, deadline
from motivation.models import Achievement


# Create your models here.
class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def check_achievements(self):
        user = self.user
        achievements = Achievement.objects.all()
        for achievement in achievements:
            conditions = achievement.conditions
            if conditions.get("type") == "task_completion":
                task_completion.check_task_completion_achievement(user, achievement, conditions)
            elif conditions.get("type") == "streak":
                streak.check_streak_achievement(user, achievement, conditions)
            elif conditions.get("type") == "time_based":
                time_based.check_time_based_achievement(self, user, achievement, conditions)
            elif conditions.get("type") == "day_of_week":
                day_of_week.check_day_of_week_achievement(user, achievement, conditions)
            elif conditions.get("type") == "holiday":
                holiday.check_holiday_achievement(user, achievement, conditions)
            elif conditions.get("type") == "collaborative":
                collaborative.check_collaborative_achievement(user, achievement, conditions)
            elif conditions.get("type") == "priority":
                priority.check_priority_achievement(self, user, achievement, conditions)
            elif conditions.get("type") == "category":
                category.check_category_achievement(user, achievement, conditions)
            elif conditions.get("type") == "deadline":
                deadline.check_deadline_achievement(self, user, achievement, conditions)