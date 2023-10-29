from django.db import models
from ..usuario.models import User
from ..publicacion.models import Publicacion


# Create your models here.

class Votacion(models.Model):
    """Model definition for Votacion"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    voto = models.IntegerField(choices=[(1, 'Me gusta'), (-1, 'No me gusta')])

    class Meta:
        """Meta definition for Votacion"""

        verbose_name = 'Votacion'
        verbose_name_plural = 'Votaciones'

    def __str__(self):
        """Unicode representantion of Votacion"""
        return str(self.voto) + " a la publicación " + str(self.publicacion)
