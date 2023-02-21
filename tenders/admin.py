from django.contrib import admin
from . import models

from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(models.Tender)
class TenderAdmin(admin.ModelAdmin):
    ...


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file")
