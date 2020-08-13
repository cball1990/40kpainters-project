from django.test import TestCase
from review.models import add_rev
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

# models test
class add_revTest(TestCase):

    def create_add_rev(self, body="test",  score="3"):
        self.u1 = User.objects.create(username='user1')
        self.up1 = UserProfile.objects.create(user=self.u1)
        return add_rev.objects.create(name=self.up1, body=body, pub_date=timezone.now(), score=score)

    def test_add_rev_creation(self):
        w = self.create_add_rev()
        self.assertTrue(isinstance(w, add_rev))
        self.assertEqual(w.__unicode__(), w.name)