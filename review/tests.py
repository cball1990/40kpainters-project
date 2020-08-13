from django.test import TestCase
from review.models import add_rev
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

# models test
class ReviewTest(TestCase):
    
    def create_review(self, name="dave", body="test",  score="3"):
        return Review.objects.create(name=name, body=body, pub_date=timezone.now(), score=score)

    def test_review_creation(self):
        w = self.create_Review()
        self.assertTrue(isinstance(w, Review))
        self.assertEqual(w.__unicode__(), w.name)