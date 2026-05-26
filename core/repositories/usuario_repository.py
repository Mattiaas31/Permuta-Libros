from core.models.usuarios import Usuario


class UsuarioRepository:

    def get_all(self):
        return Usuario.objects.all()

    def get_by_id(self, id_usuario):
        return Usuario.objects.filter(id_usuario=id_usuario).first()

    def get_by_email(self, email):
        return Usuario.objects.filter(email=email).first()

    def get_activos(self):
        return Usuario.objects.filter(activo=True)

    def create(self, nombre, apellido, email):
        return Usuario.objects.create(nombre=nombre, apellido=apellido, email=email)

    def update(self, id_usuario, **kwargs):
        Usuario.objects.filter(id_usuario=id_usuario).update(**kwargs)
        return self.get_by_id(id_usuario)

    def delete(self, id_usuario):
        Usuario.objects.filter(id_usuario=id_usuario).delete()
