from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from main.models import Club, Country

class ClubModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_country = Country.objects.create(name="Test Country")
        cls.club = Club.objects.create(
            name="Test Club",
            logo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            president="Test President",
            coach="Test Coach",
            found_date=timezone.now(),
            max_import=1000000.0,
            max_export=2000000.0,
            country=test_country
        )
