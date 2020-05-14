from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User

Paint_Choices = (
    ('basic','Basic'),
    ('tabletop', 'Table Top'),
    ('display','Display'),
)

Base_Choices = (
    ('sand','Sand'),
    ('mud', 'Mud'),
    ('concrete','Concrete'),
    ('grass','Grass'),
    ('rubble','Rubble'),
    ('snow','Snow'),
    ('none','None')
)
Status_Choices= (
    ('ordered','Ordered'),
    ('painted','Painting Complete'),
    ('basing','Basing Complete'),
    ('finishing','Final Touches'),
    ('complete','Waiting To Be Shipped'),
    ('shipped','Shipped')

)
class orderForm(models.Model):
    paintlevel = models.CharField(max_length=15, choices=Paint_Choices, default='basic')
    paintnum = models.IntegerField()
    build = models.BooleanField()
    base = models.BooleanField()
    comments = models.TextField(max_length=2000)
    basetype = models.CharField(max_length=15, choices=Base_Choices, default='none')
    scheme = models.TextField(max_length=500)
    adnum = models.CharField(max_length=60)
    adfirstline = models.CharField(max_length=100)
    adtown = models.CharField(max_length=70)
    adpostcode = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=Status_Choices, default='ordered')
    orderdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return str(self.user)


