from django.db import models


class DeletableQueryManager(models.Manager):
    def get_queryset(self):
        return super(DeletableQueryManager, self).get_queryset().filter(is_deleted__in=[False])

    def get_deleted(self):
        return super(DeletableQueryManager, self).get_queryset().filter(is_deleted__in=[True])
