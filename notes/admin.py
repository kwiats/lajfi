# -*- coding: utf-8 -*-
from django.contrib import admin

from notes.models import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'is_deleted',
        'uuid',
        'created_at',
        'updated_at',
        'title',
        'content',
        'user',
        'status',
    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
        'user',
        'status',
    )
    date_hierarchy = 'created_at'
