from django.core.files.base import ContentFile
from django.utils.six import b
from django.test import TestCase

from wagtail.wagtaildocs.models import Document, document_served

from downloadcounter.models import DownloadCount


class TestCounter(TestCase):
    def test_count(self):
        fake_file = ContentFile(b("Example document"))
        fake_file.name = 'test.txt'
        document = Document.objects.create(title="Test document", file=fake_file)
        counter = DownloadCount.objects.create(file=document)
        assert counter.count is 0
        document_served.send(sender=Document, instance=document)
        counter.refresh_from_db()
        assert counter.count is 1
