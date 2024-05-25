from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


class Notes(BaseModel):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ["-updated_at"]

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.content[:50]
        self.title = self.title.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
