from django import forms
from first_app import models


class Details(forms.ModelForm):
    class Meta:
        model=models.Comment()
        fields=["user","comment"]
