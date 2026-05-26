from core.repositories.historial_eventos_repository import HistorialEventoRepository
from core.repositories.historial_repository import HistorialRepository


class HistorialEventoService:

    def __init__(self):
        self.repository = HistorialEventoRepository()
        self.historial_repository = HistorialRepository()

    def listar_eventos(self):
        return self.repository.get_all()

    def listar_por_historial(self, id_historial):
        return self.repository.get_by_historial(id_historial)

    def obtener_evento(self, id_evento):
        evento = self.repository.get_by_id(id_evento)
        if not evento:
            raise ValueError(f"No existe un evento con id {id_evento}")
        return evento

    def registrar_evento(self, id_historial, tipo_evento, descripcion, fecha_evento):
        historial = self.historial_repository.get_by_id(id_historial)
        if not historial:
            raise ValueError(f"No existe un historial con id {id_historial}")
        return self.repository.create(
            tipo_evento=tipo_evento,
            descripcion=descripcion,
            fecha_evento=fecha_evento,
            historial_libro=historial,
        )

    def eliminar_evento(self, id_evento):
        self.obtener_evento(id_evento)
        return self.repository.delete(id_evento)
