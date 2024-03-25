from django import forms
from .models import ModelForm

class ModelForm(forms.DcModel):
    class Meta:
        model = DcModel
        fields = ['name', 'heroic_name']
