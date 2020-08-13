from django.test import TestCase
from review.models import add_rev
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

# models test
class add_revTest(TestCase):
    
    def create_add_rev(self, name="dave", body="test",  score="3"):
        return add_rev.objects.create(name=name, body=body, pub_date=timezone.now(), score=score)

    def test_add_rev_creation(self):
        w = self.create_add_rev()
        self.assertTrue(isinstance(w, add_rev))
        self.assertEqual(w.__unicode__(), w.name)