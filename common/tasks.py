import logging

from celery import shared_task
from django.utils import timezone

from common.models import EmailLog, ScheduledEmail

logger = logging.getLogger(__name__)


@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    logger.info(f"Starting send_email_task with subject '{subject}' to recipients: {recipient_list}")

    email_log = EmailLog(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=",".join(recipient_list),
        status='pending'
    )
    email_log.save()

    email_log.send_email()


@shared_task
def send_scheduled_emails():
    logger.info(f"Starting send_scheduled_emails")

    now = timezone.now()
    scheduled_emails = ScheduledEmail.objects.filter(status='pending', scheduled_time__lte=now)
    for scheduled_email in scheduled_emails:
        scheduled_email.send_email()
