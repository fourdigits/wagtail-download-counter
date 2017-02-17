from __future__ import unicode_literals

from django.db import models
from wagtail.wagtaildocs.models import Document


class DownloadCount(models.Model):
    file = models.OneToOneField(Document, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
