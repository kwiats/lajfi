# -*- coding: utf-8 -*-
from django.contrib import admin

from task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'is_deleted',
        'uuid',
        'created_at',
        'updated_at',
        'user',
        'title',
        'description',
        'priority',
        'due_date',
        'completed',
    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
        'user',
        'due_date',
        'completed',
    )
    date_hierarchy = 'created_at'
