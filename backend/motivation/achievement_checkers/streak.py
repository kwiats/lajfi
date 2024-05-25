import datetime
from django.utils.timezone import now
from motivation.models import UserAchievement

def check_streak_achievement(user, achievement, conditions):
    from task.models import Task  # dynamiczny import

    today = now().date()
    streak_days = conditions.get("days", 0)
    if streak_days > 0:
        start_date = today - datetime.timedelta(days=streak_days)
        tasks_completed = Task.objects.filter(user=user, completed=True, due_date__range=[start_date, today]).count()
        if tasks_completed >= streak_days:
            if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                UserAchievement.objects.create(user=user, achievement=achievement)
