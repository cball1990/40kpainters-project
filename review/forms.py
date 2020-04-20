from django import forms
from .models import add_review

class orderform(forms.Form):
    name = forms.ForeignKey(User, widget=forms.HiddenInput())
