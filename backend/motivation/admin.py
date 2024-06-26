# -*- coding: utf-8 -*-
from django.contrib import admin

from motivation.models import Achievement, UserAchievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created_at',
        'updated_at',
        'title',
        'description',
        'points',
        'is_deleted',

    )
    list_filter = ('is_deleted', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'achievement',
        'user',
        'date_earned',
        'is_notified',
    )
    list_filter = (
        'is_deleted',
        'achievement',
        'user',
        'date_earned',
    )
    date_hierarchy = 'created_at'
