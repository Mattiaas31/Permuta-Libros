from core.repositories.categoria_repository import CategoriaRepository


class CategoriaService:

    def __init__(self):
        self.repository = CategoriaRepository()

    def listar_categorias(self):
        return self.repository.get_all()

    def obtener_categoria(self, id_categoria):
        categoria = self.repository.get_by_id(id_categoria)
        if not categoria:
            raise ValueError(f"No existe una categoría con id {id_categoria}")
        return categoria

    def crear_categoria(self, nombre_categoria):
        if self.repository.get_by_nombre(nombre_categoria):
            raise ValueError(f"Ya existe una categoría con el nombre '{nombre_categoria}'")
        return self.repository.create(nombre_categoria=nombre_categoria)

    def actualizar_categoria(self, id_categoria, nombre_categoria):
        self.obtener_categoria(id_categoria)
        existente = self.repository.get_by_nombre(nombre_categoria)
        if existente and existente.id_categoria != id_categoria:
            raise ValueError(f"Ya existe una categoría con el nombre '{nombre_categoria}'")
        return self.repository.update(id_categoria, nombre_categoria=nombre_categoria)

    def eliminar_categoria(self, id_categoria):
        self.obtener_categoria(id_categoria)
        return self.repository.delete(id_categoria)
