from django.db import models

class SolicitudPermutas(models.Model):

    id_solicitud=models.BigAutoField(primary_key=True)
    
    usuario_solicitante=models.ForeignKey("Usuario",on_delete=models.CASCADE,related_name="solicitud_solicitada")
    usuario_receptor=models.ForeignKey("Usuario",on_delete=models.CASCADE,related_name="solicitud_recibida")
    
    libros_solicitados=models.ManyToManyField("Libro",related_name="solicitudes_donde_fue_solicitado")
    libros_ofrecidos=models.ManyToManyField("Libro",related_name="solicitud_donde_fue_ofrecido")

    def __str__(self):
        return f"{self.usuario_solicitante} solicita permuta a {self.usuario_receptor}"