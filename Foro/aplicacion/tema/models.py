from django.db import models
from ..foro.models import Foro
from ..usuario.models import User

# Create your models here.

class Tema(models.Model):
    """Model definition for Tema"""
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Tema"""

        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        """Unicode representantion of Tema"""
        return self.titulo + " " + str(self.fecha_creacion)