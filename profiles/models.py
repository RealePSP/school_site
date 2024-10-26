from django.db import models
from klasses.models import Klass

class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    klass = models.ForeignKey(Klass, related_name='profiles', on_delete=models.CASCADE, verbose_name="Класс")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='profiles/', verbose_name="Фото")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return self.name
