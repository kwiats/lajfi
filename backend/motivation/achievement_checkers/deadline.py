from motivation.models import UserAchievement

def check_deadline_achievement(task, user, achievement, conditions):
    if "early_by" in conditions:
        early_by_days = conditions.get("early_by")
        if task.completed and (task.due_date - task.created_at).days >= early_by_days:
            if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                UserAchievement.objects.create(user=user, achievement=achievement)
    if "on_time" in conditions:
        if task.completed and (task.due_date.date() == task.created_at.date()):
            if not UserAchievement.objects.filter(user=user, achievement=achievement).exists():
                UserAchievement.objects.create(user=user, achievement=achievement)
