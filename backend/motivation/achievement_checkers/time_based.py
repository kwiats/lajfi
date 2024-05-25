import datetime
from motivation.models import UserAchievement

def check_time_based_achievement(task, user, achievement, conditions):
    from task.models import Task  # dynamiczny import

    if "time" in conditions:
        target_time = conditions.get("time")
        if task.completed and task.due_date.time() <= datetime.datetime.strptime(target_time, "%H:%M").time():
            if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                UserAchievement.objects.create(user=user, achievement=achievement)
    if "time_limit" in conditions:
        time_limit_hours = conditions.get("time_limit")
        if task.completed and (task.due_date - task.created_at).total_seconds() <= time_limit_hours * 3600:
            if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                UserAchievement.objects.create(user=user, achievement=achievement)
