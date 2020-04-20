from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import order_form
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
class orderform(forms.Form):
    paintlevel = forms.ChoiceField(choices=Paint_Choices, initial='basic')
    paintnum = forms.IntegerField()
    build = forms.BooleanField()
    base = forms.BooleanField()
    comments = forms.CharField(max_length=2000, widget=forms.Textarea(
        attrs={
            "rows":10,
             "columns": 10
            }
            ))
    basetype = forms.ChoiceField(choices=Base_Choices, initial='none')
    scheme = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={
            "rows":10,
             "columns": 10
            }
            ))
    adnum = forms.CharField(max_length=60)
    adfirstline = forms.CharField(max_length=100)
    adtown = forms.CharField(max_length=70)
    adpostcode = forms.CharField(max_length=8)
    user = forms.CharField(widget=forms.HiddenInput())


