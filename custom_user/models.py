from django.contrib.auth.models import AbstractUser
from django.db import models
from klasses.models import Klass

class CustomUser(AbstractUser):
    klass = models.ForeignKey(Klass, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
