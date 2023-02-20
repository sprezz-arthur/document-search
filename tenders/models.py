from django.db import models

class Tender(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    files = models.ManyToManyField("File")

class File(models.Model):
    file = models.FileField(upload_to='documents/')