from django.shortcuts import render


def home(request):
    """
    Vista temporal con datos hardcodeados.
    Después conectamos LibroService y CategoriaService.
    """
    libros = [
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "categoria": "Ficción literaria",
            "estado": "Buen estado",
            "duenio": "carlos_r",
        },
        {
            "titulo": "El nombre de la rosa",
            "autor": "Umberto Eco",
            "categoria": "Histórica",
            "estado": "Muy buen estado",
            "duenio": "lector_anónimo",
        },
        {
            "titulo": "Ficciones",
            "autor": "Jorge Luis Borges",
            "categoria": "Cuentos",
            "estado": "Excelente estado",
            "duenio": "biblio_sur",
        },
        {
            "titulo": "El Aleph",
            "autor": "Jorge Luis Borges",
            "categoria": "Cuentos",
            "estado": "Buen estado",
            "duenio": "maria_v",
        },
        {
            "titulo": "Rayuela",
            "autor": "Julio Cortázar",
            "categoria": "Ficción literaria",
            "estado": "Regular estado",
            "duenio": "lector_sur",
        },
    ]

    categorias = [
        "Ficción literaria",
        "Historia & Ensayo",
        "Ciencia & Técnica",
        "Poesía",
        "Infantil & Juvenil",
        "Cuentos",
        "Histórica",
    ]

    context = {
        "libros": libros,
        "categorias": categorias,
        "total_disponibles": len(libros),
    }

    return render(request, "home.html", context)
