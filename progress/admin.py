# -*- coding: utf-8 -*-
from django.contrib import admin

from progress.models import Progress


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = (
        'is_deleted',
        'uuid',
        'created_at',
        'updated_at',
        'task',
        'progress',
    )
    list_filter = ('is_deleted', 'created_at', 'updated_at', 'task')
    date_hierarchy = 'created_at'
