from django.db import models
from django.contrib.auth.models import User

class add_review(model.Models):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2000)
    img = models.ImageFiled()

    def __str__(self):
            return self.user

    def pub_date_pretty(self):
            return self.pub_date.strftime('%b %e %Y')