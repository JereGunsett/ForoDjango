from django.db import models


# Create your models here.

class Foro(models.Model):
    """Model definition for Foro"""

    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()

    class Meta:
        """Meta definition for Foro"""

        verbose_name = 'Foro'
        verbose_name_plural = 'Foros'

    def __str__(self):
        """Unicode representantion of MODELNAME"""
        return self.nombre
