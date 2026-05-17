from django.db import models

class Historial(models.Model):
    id_historial=models.BigAutoField(primary_key=True)
    libro=models.OneToOneField("Libro",on_delete=models.CASCADE,related_name="historial")
    cantidad_permutas=models.IntegerField(default=0)

      
    def __str__(self):
        return f"{self.libro.titulo}"

