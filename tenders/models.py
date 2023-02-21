from django.db import models


from django.utils.html import format_html


class Tender(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    files = models.ManyToManyField("File", blank=True)


class File(models.Model):
    file = models.FileField(upload_to="tenders/")
    contents = models.TextField(blank=True, null=True)
