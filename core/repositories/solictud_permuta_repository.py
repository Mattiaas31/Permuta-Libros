from core.models.solicitud_permutas import SolicitudPermutas


class SolicitudPermutaRepository:

    def get_all(self):
        return SolicitudPermutas.objects.select_related(
            "usuario_solicitante", "usuario_receptor"
        ).prefetch_related("libros_solicitados", "libros_ofrecidos").all()

    def get_by_id(self, id_solicitud):
        return SolicitudPermutas.objects.select_related(
            "usuario_solicitante", "usuario_receptor"
        ).prefetch_related("libros_solicitados", "libros_ofrecidos").filter(id_solicitud=id_solicitud).first()

    def get_by_solicitante(self, id_usuario):
        return SolicitudPermutas.objects.select_related(
            "usuario_solicitante", "usuario_receptor"
        ).prefetch_related("libros_solicitados", "libros_ofrecidos").filter(usuario_solicitante_id=id_usuario)

    def get_by_receptor(self, id_usuario):
        return SolicitudPermutas.objects.select_related(
            "usuario_solicitante", "usuario_receptor"
        ).prefetch_related("libros_solicitados", "libros_ofrecidos").filter(usuario_receptor_id=id_usuario)

    def create(self, usuario_solicitante, usuario_receptor, libros_solicitados, libros_ofrecidos):
        solicitud = SolicitudPermutas.objects.create(
            usuario_solicitante=usuario_solicitante,
            usuario_receptor=usuario_receptor,
        )
        solicitud.libros_solicitados.set(libros_solicitados)
        solicitud.libros_ofrecidos.set(libros_ofrecidos)
        return solicitud

    def update_libros(self, id_solicitud, libros_solicitados=None, libros_ofrecidos=None):
        solicitud = self.get_by_id(id_solicitud)
        if libros_solicitados is not None:
            solicitud.libros_solicitados.set(libros_solicitados)
        if libros_ofrecidos is not None:
            solicitud.libros_ofrecidos.set(libros_ofrecidos)
        return solicitud

    def delete(self, id_solicitud):
        SolicitudPermutas.objects.filter(id_solicitud=id_solicitud).delete()