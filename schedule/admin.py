# -*- coding: utf-8 -*-
from django.contrib import admin

from schedule.models import  Event



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created_at',
        'updated_at',
        'user',
        'title',
        'description',
        'start_time',
        'end_time',
        'is_deleted',

    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
        'user',
        'start_time',
        'end_time',
    )
    date_hierarchy = 'created_at'
