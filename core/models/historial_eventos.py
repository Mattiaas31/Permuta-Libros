from django.db import models

class HistorialEvento(models.Model):

    id_evento=models.BigAutoField(primary_key=True)
    tipo_evento=models.CharField(max_length=100)
    descripcion=models.TextField()
    fecha_evento=models.DateField()
    historial_libro=models.ForeignKey("Historial",on_delete=models.CASCADE,related_name="eventos")

    def __str__(self):
        return f"{self.fecha_evento} | {self.tipo_evento} | {self.historial_libro.libro.titulo}"