from django.db import models
from ..usuario.models import User
from ..tema.models import Tema



# Create your models here.

class Publicacion(models.Model):
    """Model definition for Publicacion"""
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Publicacion"""

        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        """Unicode representantion of Publicacion"""
        return str(self.tema) + " " + str(self.autor)