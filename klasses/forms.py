from django import forms
from .models import Klass

class KlassForm(forms.ModelForm):
    class Meta:
        model = Klass
        fields = ['name', 'description']
