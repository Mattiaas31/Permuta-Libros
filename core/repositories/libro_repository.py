from core.models.libros import Libro


class LibroRepository:

    def get_all(self):
        return Libro.objects.select_related("duenio", "categoria").all()

    def get_by_id(self, id_libro):
        return Libro.objects.select_related("duenio", "categoria").filter(id_libro=id_libro).first()

    def get_disponibles(self):
        return Libro.objects.select_related("duenio", "categoria").filter(disponible=True)

    def get_by_duenio(self, id_usuario):
        return Libro.objects.select_related("duenio", "categoria").filter(duenio_id=id_usuario)

    def get_by_categoria(self, id_categoria):
        return Libro.objects.select_related("duenio", "categoria").filter(categoria_id=id_categoria)

    def create(self, **kwargs):
        return Libro.objects.create(**kwargs)

    def update(self, id_libro, **kwargs):
        Libro.objects.filter(id_libro=id_libro).update(**kwargs)
        return self.get_by_id(id_libro)

    def delete(self, id_libro):
        Libro.objects.filter(id_libro=id_libro).delete()
