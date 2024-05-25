# -*- coding: utf-8 -*-
from django.contrib import admin

from reminder.models import  Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = (
        'is_deleted',
        'uuid',
        'created_at',
        'updated_at',
        'user',
        'title',
        'description',
        'remind_at',
    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
        'user',
        'remind_at',
    )
    date_hierarchy = 'created_at'
