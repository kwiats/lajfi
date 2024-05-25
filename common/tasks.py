import logging

from celery import shared_task
from django.core.mail import send_mail

from common.models import EmailLog

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
