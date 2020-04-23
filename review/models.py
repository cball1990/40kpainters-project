from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField, JPEGField

class add_rev(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2000)
    img = StdImageField(upload_to='images/',
                          variations={'resized': {'width': 250, 'height': 250 , "crop": True}})
    score = models.IntegerField(default=1)

    def pub_date_pretty(self):
            return self.pub_date.strftime('%b %e %Y')