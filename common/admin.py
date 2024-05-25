# -*- coding: utf-8 -*-
from django.contrib import admin

from common.models import EmailLog, ScheduledEmail
def send_email_action(modeladmin, request, queryset):
    for email_instance in queryset:
        email_instance.send_email()

send_email_action.short_description = "Send selected emails"

@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created_at',
        'updated_at',
        'subject',
        'message',
        'from_email',
        'recipient_list',
        'sent_at',
        'status',
        'error_message',
        'is_deleted',
    )
    list_filter = ('is_deleted', 'created_at', 'updated_at', 'sent_at')
    date_hierarchy = 'created_at'
    actions = [send_email_action]  # Register the action


@admin.register(ScheduledEmail)
class ScheduledEmailAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created_at',
        'updated_at',
        'subject',
        'message',
        'from_email',
        'recipient_list',
        'scheduled_time',
        'status',
        'error_message',
        'is_deleted',

    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
        'scheduled_time',
    )
    date_hierarchy = 'created_at'
    actions = [send_email_action]  # Register the action
