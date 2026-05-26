from core.repositories.solictud_permuta_repository import SolicitudPermutaRepository
from core.repositories.usuario_repository import UsuarioRepository
from core.repositories.libro_repository import LibroRepository


class SolicitudPermutaService:

    def __init__(self):
        self.repository = SolicitudPermutaRepository()
        self.usuario_repository = UsuarioRepository()
        self.libro_repository = LibroRepository()

    def listar_solicitudes(self):
        return self.repository.get_all()

    def listar_por_solicitante(self, id_usuario):
        return self.repository.get_by_solicitante(id_usuario)

    def listar_por_receptor(self, id_usuario):
        return self.repository.get_by_receptor(id_usuario)

    def obtener_solicitud(self, id_solicitud):
        solicitud = self.repository.get_by_id(id_solicitud)
        if not solicitud:
            raise ValueError(f"No existe una solicitud con id {id_solicitud}")
        return solicitud

    def crear_solicitud(self, id_solicitante, id_receptor, ids_libros_solicitados, ids_libros_ofrecidos):
        solicitante = self.usuario_repository.get_by_id(id_solicitante)
        if not solicitante:
            raise ValueError(f"No existe el usuario solicitante con id {id_solicitante}")
        receptor = self.usuario_repository.get_by_id(id_receptor)
        if not receptor:
            raise ValueError(f"No existe el usuario receptor con id {id_receptor}")
        if id_solicitante == id_receptor:
            raise ValueError("El solicitante y el receptor no pueden ser el mismo usuario")

        libros_solicitados = [self.libro_repository.get_by_id(id) for id in ids_libros_solicitados]
        if None in libros_solicitados:
            raise ValueError("Uno o más libros solicitados no existen")

        libros_ofrecidos = [self.libro_repository.get_by_id(id) for id in ids_libros_ofrecidos]
        if None in libros_ofrecidos:
            raise ValueError("Uno o más libros ofrecidos no existen")

        return self.repository.create(
            usuario_solicitante=solicitante,
            usuario_receptor=receptor,
            libros_solicitados=libros_solicitados,
            libros_ofrecidos=libros_ofrecidos,
        )

    def actualizar_libros(self, id_solicitud, ids_libros_solicitados=None, ids_libros_ofrecidos=None):
        self.obtener_solicitud(id_solicitud)
        libros_solicitados = None
        libros_ofrecidos = None
        if ids_libros_solicitados is not None:
            libros_solicitados = [self.libro_repository.get_by_id(id) for id in ids_libros_solicitados]
            if None in libros_solicitados:
                raise ValueError("Uno o más libros solicitados no existen")
        if ids_libros_ofrecidos is not None:
            libros_ofrecidos = [self.libro_repository.get_by_id(id) for id in ids_libros_ofrecidos]
            if None in libros_ofrecidos:
                raise ValueError("Uno o más libros ofrecidos no existen")
        return self.repository.update_libros(id_solicitud, libros_solicitados, libros_ofrecidos)

    def eliminar_solicitud(self, id_solicitud):
        self.obtener_solicitud(id_solicitud)
        return self.repository.delete(id_solicitud)
