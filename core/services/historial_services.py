from core.repositories.historial_repository import HistorialRepository
from core.repositories.libro_repository import LibroRepository


class HistorialService:

    def __init__(self):
        self.repository = HistorialRepository()
        self.libro_repository = LibroRepository()

    def listar_historiales(self):
        return self.repository.get_all()

    def obtener_historial(self, id_historial):
        historial = self.repository.get_by_id(id_historial)
        if not historial:
            raise ValueError(f"No existe un historial con id {id_historial}")
        return historial

    def obtener_por_libro(self, id_libro):
        historial = self.repository.get_by_libro(id_libro)
        if not historial:
            raise ValueError(f"No existe historial para el libro con id {id_libro}")
        return historial

    def crear_historial(self, id_libro):
        libro = self.libro_repository.get_by_id(id_libro)
        if not libro:
            raise ValueError(f"No existe un libro con id {id_libro}")
        if self.repository.get_by_libro(id_libro):
            raise ValueError(f"El libro con id {id_libro} ya tiene un historial")
        return self.repository.create(libro=libro)

    def incrementar_permutas(self, id_historial):
        self.obtener_historial(id_historial)
        return self.repository.incrementar_permutas(id_historial)

    def eliminar_historial(self, id_historial):
        self.obtener_historial(id_historial)
        return self.repository.delete(id_historial)
