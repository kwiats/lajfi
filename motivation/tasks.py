import logging

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from motivation.models import UserAchievement

logger = logging.getLogger(__name__)


@shared_task
def check_new_achievements():
    logger.info("Starting the check_new_achievements task.")

    try:
        new_achievements = UserAchievement.objects.filter(is_notified=False)
        logger.info(f"Found {new_achievements.count()} new achievements to process.")

        for user_achievement in new_achievements:
            user = user_achievement.user
            achievement = user_achievement.achievement

            logger.info(f"Processing achievement '{achievement.title}' for user '{user.username}'.")

            try:
                send_mail(
                    'Congratulations on your achievement!',
                    f'Hi {user.username},\n\nCongratulations on earning the "{achievement.title}" achievement!\n\nKeep up the great work!\n\nBest regards,\nYour Team',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,
                )
                user_achievement.is_notified = True
                user_achievement.save()
                logger.info(f"Successfully notified user '{user.username}' for achievement '{achievement.title}'.")
            except Exception as e:
                logger.error(
                    f"Error sending email to user '{user.username}' for achievement '{achievement.title}': {e}")

    except Exception as e:
        logger.error(f"Error in check_new_achievements task: {e}")

    logger.info("Completed the check_new_achievements task.")