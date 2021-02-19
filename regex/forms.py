from . import models
from django import forms

class regforms(forms.ModelForm):
    class Meta:
        model=models.Texts
        fields=('maintext','searchtext')
