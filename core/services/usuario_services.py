from core.repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()

    def listar_usuarios(self):
        return self.repository.get_all()

    def listar_activos(self):
        return self.repository.get_activos()

    def obtener_usuario(self, id_usuario):
        usuario = self.repository.get_by_id(id_usuario)
        if not usuario:
            raise ValueError(f"No existe un usuario con id {id_usuario}")
        return usuario

    def obtener_por_email(self, email):
        usuario = self.repository.get_by_email(email)
        if not usuario:
            raise ValueError(f"No existe un usuario con email {email}")
        return usuario

    def crear_usuario(self, nombre, apellido, email):
        if self.repository.get_by_email(email):
            raise ValueError(f"Ya existe un usuario con el email {email}")
        return self.repository.create(nombre=nombre, apellido=apellido, email=email)

    def actualizar_usuario(self, id_usuario, **kwargs):
        self.obtener_usuario(id_usuario)
        if "email" in kwargs:
            existente = self.repository.get_by_email(kwargs["email"])
            if existente and existente.id_usuario != id_usuario:
                raise ValueError(f"El email {kwargs['email']} ya está en uso")
        return self.repository.update(id_usuario, **kwargs)

    def desactivar_usuario(self, id_usuario):
        self.obtener_usuario(id_usuario)
        return self.repository.update(id_usuario, activo=False)

    def eliminar_usuario(self, id_usuario):
        self.obtener_usuario(id_usuario)
        return self.repository.delete(id_usuario)
