from django.db import models

# Create your models here.
from django.db import models

class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre