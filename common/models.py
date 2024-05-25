import logging
import uuid

from django.core.mail import send_mail
from django.db import DEFAULT_DB_ALIAS
from django.db import models
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords

from common.manager import DeletableQueryManager

logger = logging.getLogger(__name__)


class IPAddressHistoricalModel(models.Model):
    ip_address = models.GenericIPAddressField(_('IP address'))

    class Meta:
        abstract = True


class DeletableModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = DeletableQueryManager()
    default_manager = models.Manager()

    def delete(self, using=DEFAULT_DB_ALIAS, keep_parents=False):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class BaseModel(DeletableModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    history = HistoricalRecords(bases=[IPAddressHistoricalModel, ], inherit=True, )

    class Meta:
        abstract = True


class EmailLog(BaseModel):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    recipient_list = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('success', 'Success'), ('failure', 'Failure')])
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} to {self.recipient_list}"

    def send_email(self):
        logger.info(f"Starting send_email with subject '{self.subject}' to recipients: {self.recipient_list}")

        recipient_list = self.recipient_list.split(",")

        try:
            send_mail(
                self.subject,
                self.message,
                self.from_email,
                recipient_list,
                fail_silently=False,
            )
            self.status = 'success'
            logger.info(f"Email with subject '{self.subject}' successfully sent to {self.recipient_list}")
        except Exception as e:
            self.status = 'failure'
            self.error_message = str(e)
            logger.error(f"Error sending email with subject '{self.subject}' to {self.recipient_list}: {e}")

        self.save()


class ScheduledEmail(BaseModel):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    recipient_list = models.TextField()
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')],
                              default='pending')
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} to {self.recipient_list} at {self.scheduled_time}"

    def send_email(self):
        logger.info(f"Starting send_email with subject '{self.subject}' to recipients: {self.recipient_list}")

        email_log = EmailLog(
            subject=self.subject,
            message=self.message,
            from_email=self.from_email,
            recipient_list=self.recipient_list,
            status='pending'
        )
        email_log.save()
        email_log.send_email()
