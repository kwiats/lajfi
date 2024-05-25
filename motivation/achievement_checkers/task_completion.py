from motivation.models import UserAchievement


def check_task_completion_achievement(user, achievement, conditions):
    from task.models import Task  # dynamiczny import

    task_count = Task.objects.filter(user=user, completed=True).count()
    if task_count >= conditions.get("count", 0):
        if not UserAchievement.objects.filter(user=user, achievement=achievement, is_awarded=True).exists():
            UserAchievement.objects.create(user=user, achievement=achievement, is_awarded=True)
