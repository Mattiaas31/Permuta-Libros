from core.models.historial_eventos import HistorialEvento


class HistorialEventoRepository:

    def get_all(self):
        return HistorialEvento.objects.select_related("historial_libro__libro").all()

    def get_by_id(self, id_evento):
        return HistorialEvento.objects.select_related("historial_libro__libro").filter(id_evento=id_evento).first()

    def get_by_historial(self, id_historial):
        return HistorialEvento.objects.filter(historial_libro_id=id_historial).order_by("-fecha_evento")

    def create(self, tipo_evento, descripcion, fecha_evento, historial_libro):
        return HistorialEvento.objects.create(
            tipo_evento=tipo_evento,
            descripcion=descripcion,
            fecha_evento=fecha_evento,
            historial_libro=historial_libro,
        )

    def update(self, id_evento, **kwargs):
        HistorialEvento.objects.filter(id_evento=id_evento).update(**kwargs)
        return self.get_by_id(id_evento)

    def delete(self, id_evento):
        evento = self.get_by_id(id_evento)
        if evento:
            evento.delete()
            return True
        return False
