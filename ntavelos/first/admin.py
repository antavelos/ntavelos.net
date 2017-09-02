# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from first.models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created',)
    fields = ('name', 'file', 'notes', 'created',)
    readonly_fields = ('created', 'name',)

    def name(self, obj):
        return obj.name
    name.short_description = 'Name'
