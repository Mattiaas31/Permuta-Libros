from core.models.permuta import Permuta


class PermutaRepository:

    def get_all(self):
        return Permuta.objects.select_related("solicitud").all()

    def get_by_id(self, id_permuta):
        return Permuta.objects.select_related("solicitud").filter(id_permuta=id_permuta).first()

    def get_by_estado(self, estado):
        return Permuta.objects.select_related("solicitud").filter(estado=estado)

    def get_by_solicitud(self, id_solicitud):
        return Permuta.objects.filter(solicitud_id=id_solicitud).first()

    def create(self, fecha_confirmacion, solicitud, estado="pendiente"):
        return Permuta.objects.create(
            fecha_confirmacion=fecha_confirmacion,
            solicitud=solicitud,
            estado=estado,
        )

    def update_estado(self, id_permuta, estado):
        Permuta.objects.filter(id_permuta=id_permuta).update(estado=estado)
        return self.get_by_id(id_permuta)

    def update(self, id_permuta, **kwargs):
        Permuta.objects.filter(id_permuta=id_permuta).update(**kwargs)
        return self.get_by_id(id_permuta)

    def delete(self, id_permuta):
        permuta = self.get_by_id(id_permuta)
        if permuta:
            permuta.delete()
            return True
        return False
