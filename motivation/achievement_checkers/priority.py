from motivation.models import UserAchievement

def check_priority_achievement(task, user, achievement, conditions):
    if "level" in conditions:
        target_level = conditions.get("level")
        if task.completed and task.priority == target_level:
            if not UserAchievement.objects.filter(user=user, achievement=achievement, is_awarded=True).exists():
                UserAchievement.objects.create(user=user, achievement=achievement, is_awarded=True)
