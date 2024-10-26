from django.db import models
from klasses.models import Klass

class ClassNewspaper(models.Model):
    klass = models.ForeignKey(Klass, related_name='newspapers', verbose_name='Класс', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='newspapers/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
from django.db import models
