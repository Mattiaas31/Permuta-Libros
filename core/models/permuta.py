from django.db import models


class Permuta(models.Model):

    id_permuta=models.BigAutoField(primary_key=True)
    fecha_confirmacion=models.DateField()
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("finalizada", "Finalizada"),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )
    
    
    solicitud=models.OneToOneField("SolicitudPermutas", on_delete=models.PROTECT,related_name="permuta")

    def __str__(self):
        return f"Permuta #{self.id_permuta} - {self.solicitud.usuario_solicitante} con {self.solicitud.usuario_receptor} - {self.get_estado_display()}"