from motivation.models import UserAchievement

def check_day_of_week_achievement(user, achievement, conditions):
    from task.models import Task  # dynamiczny import

    days_mapping = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7,
    }

    if "days" in conditions:
        target_days = [days_mapping[day] for day in conditions.get("days", [])]
        if Task.objects.filter(user=user, completed=True, due_date__week_day__in=target_days).count() >= conditions.get("count", 0):
            if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                UserAchievement.objects.create(user=user, achievement=achievement)
