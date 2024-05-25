import uuid
from django.db import models
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords
from django.db import DEFAULT_DB_ALIAS

from common.manager import DeletableQueryManager


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
