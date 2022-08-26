from dataclasses import field
from .models import Cancer
from django import forms

class CancerForms(forms.ModelForm):
    class Meta:
        model = Cancer
        exclude = ['prediction']