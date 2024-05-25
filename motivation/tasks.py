from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from motivation.models import UserAchievement


@shared_task
def check_new_achievements():
    new_achievements = UserAchievement.objects.filter(is_notified=False)
    for user_achievement in new_achievements:
        user = user_achievement.user
        achievement = user_achievement.achievement
        send_mail(
            'Congratulations on your achievement!',
            f'Hi {user.username},\n\nCongratulations on earning the "{achievement.title}" achievement!\n\nKeep up the great work!\n\nBest regards,\nYour Team',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        user_achievement.is_notified = True
        user_achievement.save()
