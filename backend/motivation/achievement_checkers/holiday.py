from motivation.models import UserAchievement

def check_holiday_achievement(user, achievement, conditions):
    from task.models import Task  # dynamiczny import
    if conditions.get("holiday") == "any":
        # Implement logic to check if task was completed on a holiday
        pass
