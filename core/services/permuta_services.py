from django.utils import timezone
from core.repositories.permuta_repository import PermutaRepository
from core.repositories.solictud_permuta_repository import SolicitudPermutaRepository
from core.services.historial_services import HistorialService          
from core.services.historial_eventos_services import HistorialEventoService  



class PermutaService:

    def __init__(self):
        self.repository = PermutaRepository()
        self.solicitud_repository = SolicitudPermutaRepository()
        self.historial_service = HistorialService()                    
        self.historial_evento_service = HistorialEventoService() 

    def listar_permutas(self):
        return self.repository.get_all()

    def listar_por_estado(self, estado):
        return self.repository.get_by_estado(estado)

    def obtener_permuta(self, id_permuta):
        permuta = self.repository.get_by_id(id_permuta)
        if not permuta:
            raise ValueError(f"No existe una permuta con id {id_permuta}")
        return permuta

    def crear_permuta(self, id_solicitud, fecha_confirmacion):
        solicitud = self.solicitud_repository.get_by_id(id_solicitud)
        if not solicitud:
            raise ValueError(f"No existe una solicitud con id {id_solicitud}")
        if self.repository.get_by_solicitud(id_solicitud):
            raise ValueError(f"Ya existe una permuta para la solicitud {id_solicitud}")
        return self.repository.create(
            fecha_confirmacion=fecha_confirmacion,
            solicitud=solicitud,
        )

    def confirmar_permuta(self, id_permuta):
        permuta = self.obtener_permuta(id_permuta)
        if permuta.estado != "pendiente":
            raise ValueError("Solo se pueden confirmar permutas en estado 'pendiente'")
        return self.repository.update_estado(id_permuta, "confirmada")

    def cancelar_permuta(self, id_permuta):
        permuta = self.obtener_permuta(id_permuta)
        if permuta.estado == "finalizada":
            raise ValueError("No se puede cancelar una permuta ya finalizada")
        return self.repository.update_estado(id_permuta, "cancelada")

    def finalizar_permuta(self, id_permuta):
        permuta = self.obtener_permuta(id_permuta)
        if permuta.estado != "confirmada":
            raise ValueError("Solo se pueden finalizar permutas en estado 'confirmada'")
        permuta = self.repository.update_estado(id_permuta, "finalizada")
        self._registrar_evento_finalizacion(permuta)
        return permuta

    def eliminar_permuta(self, id_permuta):
        self.obtener_permuta(id_permuta)
        return self.repository.delete(id_permuta)

    def _registrar_evento_finalizacion(self, permuta):
        solicitud = permuta.solicitud
        libros = list(solicitud.libros_solicitados.all()) + list(solicitud.libros_ofrecidos.all())
        hoy = timezone.now().date()
        for libro in libros:
            try:
                historial = self.historial_service.obtener_por_libro(libro.id_libro)  
                self.historial_service.incrementar_permutas(historial.id_historial)   
                self.historial_evento_service.registrar_evento(                        
                    id_historial=historial.id_historial,
                    tipo_evento="permuta_finalizada",
                    descripcion=f"Permuta #{permuta.id_permuta} finalizada entre "
                                f"{solicitud.usuario_solicitante} y {solicitud.usuario_receptor}.",
                    fecha_evento=hoy,
                )
            except ValueError:
                pass  # el libro no tiene historial, se omite silenciosamente
