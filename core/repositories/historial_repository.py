from core.models.historial import Historial


class HistorialRepository:

    def get_all(self):
        return Historial.objects.select_related("libro").all()

    def get_by_id(self, id_historial):
        return Historial.objects.select_related("libro").filter(id_historial=id_historial).first()

    def get_by_libro(self, id_libro):
        return Historial.objects.filter(libro_id=id_libro).first()

    def create(self, libro, cantidad_permutas=0):
        return Historial.objects.create(libro=libro, cantidad_permutas=cantidad_permutas)

    def incrementar_permutas(self, id_historial):
        historial = self.get_by_id(id_historial)
        if historial:
            historial.cantidad_permutas += 1
            historial.save()
        return historial

    def update(self, id_historial, **kwargs):
        Historial.objects.filter(id_historial=id_historial).update(**kwargs)
        return self.get_by_id(id_historial)

    def delete(self, id_historial):
        historial = self.get_by_id(id_historial)
        if historial:
            historial.delete()
            return True
        return False
