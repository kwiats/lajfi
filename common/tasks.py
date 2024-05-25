from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    logger.info(f"Starting send_email_task with subject '{subject}' to recipients: {recipient_list}")

    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        logger.info(f"Email with subject '{subject}' successfully sent to {recipient_list}")
    except Exception as e:
        logger.error(f"Error sending email with subject '{subject}' to {recipient_list}: {e}")
