from django.contrib import admin
from . import models


@admin.register(models.Tender)
class TenderAdmin(admin.ModelAdmin):
    ...


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    ...