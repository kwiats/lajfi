import logging

from celery import shared_task
from django.conf import settings
from django.utils import timezone

from common.tasks import send_email_task
from reminder.models import Reminder

logger = logging.getLogger(__name__)


@shared_task
def check_and_send_reminders():
    logger.info("Starting the check_and_send_reminders task.")

    now = timezone.now()
    reminders = Reminder.objects.filter(remind_at__lte=now)
    logger.info(f"Found {reminders.count()} reminders to process.")

    for reminder in reminders:
        user = reminder.user
        title = reminder.title
        description = reminder.description

        logger.info(f"Processing reminder '{title}' for user '{user.username}'.")

        try:
            send_email_task.delay(
                f'Reminder: {title}',
                f'Hi {user.username},\n\nThis is a reminder for: {title}.\n\n{description}\n\nBest regards,\nYour Team',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            reminder.is_deleted = True
            logger.info(f"Successfully sent reminder '{title}' to user '{user.username}'.")
        except Exception as e:
            logger.error(f"Error sending reminder '{title}' to user '{user.username}': {e}")

    logger.info("Completed the check_and_send_reminders task.")
