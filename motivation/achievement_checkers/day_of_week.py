from motivation.models import UserAchievement


def check_day_of_week_achievement(user, achievement, conditions):
    from task.models import Task  # dynamiczny import

    if "days" in conditions:
        target_days = conditions.get("days")
        if Task.objects.filter(user=user, completed=True, due_date__week_day__in=target_days).count() >= conditions.get(
                "count", 0):
            if not UserAchievement.objects.filter(user=user, achievement=achievement, is_awarded=True).exists():
                UserAchievement.objects.create(user=user, achievement=achievement, is_awarded=True)
