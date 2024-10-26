from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Profile
        fields = ['name', 'description', 'photo', 'birth_date']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'photo': 'Фото',
            'birth_date': 'Дата рождения',
        }
