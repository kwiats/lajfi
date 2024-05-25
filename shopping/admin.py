# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ShoppingList, ShoppingItem


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = (
        'is_deleted',
        'uuid',
        'created_at',
        'updated_at',
        'name',
        'user',
    )
    list_filter = ('is_deleted', 'created_at', 'updated_at', 'user')
    raw_id_fields = ('items',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    list_display = (
        'uuid',
        'created_at',
        'updated_at',
        'user',
        'name',
        'quantity',
        'purchased',
        'is_deleted',

    )
    list_filter = (
        'is_deleted',
        'created_at',
        'updated_at',
        'user',
        'purchased',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
