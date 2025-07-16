from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=250)
    telefono = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} -> {self.telefono}"
