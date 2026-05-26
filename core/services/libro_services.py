from core.repositories.libro_repository import LibroRepository
from core.repositories.historial_repository import HistorialRepository


class LibroService:

    def __init__(self):
        self.repository = LibroRepository()
        self.historial_repository = HistorialRepository()

    def listar_libros(self):
        return self.repository.get_all()

    def listar_disponibles(self):
        return self.repository.get_disponibles()

    def listar_por_duenio(self, id_usuario):
        return self.repository.get_by_duenio(id_usuario)

    def listar_por_categoria(self, id_categoria):
        return self.repository.get_by_categoria(id_categoria)

    def obtener_libro(self, id_libro):
        libro = self.repository.get_by_id(id_libro)
        if not libro:
            raise ValueError(f"No existe un libro con id {id_libro}")
        return libro

    def crear_libro(self, titulo, autor, anio_publicado, editorial, descripcion, estado, genero, categoria, duenio=None, isbn=None, disponible=True):
        libro = self.repository.create(
            titulo=titulo,
            autor=autor,
            anio_publicado=anio_publicado,
            editorial=editorial,
            descripcion=descripcion,
            estado=estado,
            genero=genero,
            categoria=categoria,
            duenio=duenio,
            isbn=isbn,
            disponible=disponible,
        )
        self.historial_repository.create(libro=libro)
        return libro

    def actualizar_libro(self, id_libro, **kwargs):
        self.obtener_libro(id_libro)
        return self.repository.update(id_libro, **kwargs)

    def marcar_no_disponible(self, id_libro):
        self.obtener_libro(id_libro)
        return self.repository.update(id_libro, disponible=False)

    def marcar_disponible(self, id_libro):
        self.obtener_libro(id_libro)
        return self.repository.update(id_libro, disponible=True)

    def eliminar_libro(self, id_libro):
        self.obtener_libro(id_libro)
        return self.repository.delete(id_libro)
