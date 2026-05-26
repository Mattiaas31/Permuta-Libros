from core.models.categorias import Categoria


class CategoriaRepository:

    def get_all(self):
        return Categoria.objects.all()

    def get_by_id(self, id_categoria):
        return Categoria.objects.filter(id_categoria=id_categoria).first()

    def get_by_nombre(self, nombre):
        return Categoria.objects.filter(nombre_categoria__iexact=nombre).first()

    def create(self, nombre_categoria):
        return Categoria.objects.create(nombre_categoria=nombre_categoria)

    def update(self, id_categoria, nombre_categoria):
        Categoria.objects.filter(id_categoria=id_categoria).update(nombre_categoria=nombre_categoria)
        return self.get_by_id(id_categoria)

    def delete(self, id_categoria):
        categoria = self.get_by_id(id_categoria)
        if categoria:
            categoria.delete()
            return True
        return False
