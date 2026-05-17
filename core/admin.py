from django.contrib import admin
from .models import (
    Libro,
    Categoria,
    SolicitudPermutas,
    Historial,
    HistorialEvento,
    Permuta,
    Usuario

)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria","duenio")
    search_fields = ("titulo", "autor")
    list_filter = ("categoria","duenio")

    
admin.site.register(Categoria)
@admin.register(SolicitudPermutas)


class SolicitudPermutasAdmin(admin.ModelAdmin):
    list_display = (
        "id_solicitud",
        "usuario_solicitante",
        "usuario_receptor",
        "mostrar_libros_ofrecidos",
        "mostrar_libros_solicitados",
    )

    search_fields = (
        "libros_ofrecidos__titulo",
        "libros_solicitados__titulo",
    )

    list_filter = (
        "usuario_solicitante",
        "usuario_receptor",
    )

    def mostrar_libros_ofrecidos(self, obj):
        return ", ".join(libro.titulo for libro in obj.libros_ofrecidos.all())

    mostrar_libros_ofrecidos.short_description = "Libros ofrecidos"

    def mostrar_libros_solicitados(self, obj):
        return ", ".join(libro.titulo for libro in obj.libros_solicitados.all())

    mostrar_libros_solicitados.short_description = "Libros solicitados"


@admin.register(HistorialEvento)
class HistorialEventoAdmin(admin.ModelAdmin):
    list_display = ("tipo_evento", "libro", "fecha_evento", "descripcion")
    search_fields = (
        "tipo_evento",
        "descripcion",
        "historial_libro__libro__titulo",
    )
    list_filter = ("tipo_evento", "fecha_evento")

    def libro(self, obj):
        return obj.historial_libro.libro.titulo

    libro.short_description = "Libro"


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ("libro", "cantidad_permutas")
    search_fields = ("libro__titulo",)


admin.site.register(Usuario)


@admin.register(Permuta)
class PermutaAdmin(admin.ModelAdmin):
    list_display = (
        "id_permuta",
        "usuario_solicitante",
        "usuario_receptor",
        "estado",
        "fecha_confirmacion",
        "libros_ofrecidos",
        "libros_solicitados",
    )

    search_fields = (
        "estado",
        "solicitud__libros_ofrecidos__titulo",
        "solicitud__libros_solicitados__titulo",
    )

    list_filter = (
        "estado",
        "fecha_confirmacion",
    )

    def usuario_solicitante(self, obj):
        return obj.solicitud.usuario_solicitante

    usuario_solicitante.short_description = "Solicitante"

    def usuario_receptor(self, obj):
        return obj.solicitud.usuario_receptor

    usuario_receptor.short_description = "Receptor"

    def libros_ofrecidos(self, obj):
        return ", ".join(libro.titulo for libro in obj.solicitud.libros_ofrecidos.all())

    libros_ofrecidos.short_description = "Libros ofrecidos"

    def libros_solicitados(self, obj):
        return ", ".join(libro.titulo for libro in obj.solicitud.libros_solicitados.all())

    libros_solicitados.short_description = "Libros solicitados"