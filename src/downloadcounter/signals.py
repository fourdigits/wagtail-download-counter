from __future__ import absolute_import, unicode_literals

from django.dispatch import receiver
from wagtail.wagtaildocs.models import document_served

from downloadcounter.models import DownloadCount


@receiver(document_served)
def count(instance, **kwargs):
    download_count, created = DownloadCount.objects.get_or_create(file=instance)
    download_count.count = download_count.count + 1
    download_count.save()
