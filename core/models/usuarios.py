from django.db import models

class Usuario(models.Model):

    id_usuario=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    fecha_registro=models.DateField(auto_now_add=True)
    activo=models.BooleanField(default=True)

    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
