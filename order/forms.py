from django import forms
from django.forms import ModelForm
from .models import order_form

class orderform(ModelForm):
    class Meta:
        model = order_form
        comments = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":10}))
        scheme = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
        fields = ['paintlevel', 'paintnum', 'build', 'base', 'comments', 'basetype',
         'scheme', 'adnum', 'adfirstline', 'adtown', 'adpostcode']
