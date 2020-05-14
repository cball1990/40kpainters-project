from django.db import models
from stdimage import StdImageField, JPEGField

class News(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = StdImageField(upload_to='images/',
                          variations={'resized': {'width': 250, 'height': 250 , "crop": True}})

    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:150]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
