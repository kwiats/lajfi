from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


class Location(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    tags = models.ManyToManyField('Tag', blank=True, related_name='locations')

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
