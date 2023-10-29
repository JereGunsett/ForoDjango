from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """Model definition for Usuario"""

    class Meta:
        """Meta definition for Usuario"""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        """Unicode representantion of Usuario"""
        return str(self.user)