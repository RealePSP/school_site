from django import forms
from .models import ClassNewspaper

class ClassNewspaperForm(forms.ModelForm):
    class Meta:
        model = ClassNewspaper
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Изображение',
        }
