from django.db import models


class Libro(models.Model):

    titulo=models.CharField(max_length=100,null=False)
    autor=models.CharField(max_length=100)
    anio_publicado=models.IntegerField()
    editorial=models.CharField(max_length=50)
    
    isbn=models.CharField(max_length=20,unique=True,blank=True,null=True)
    descripcion=models.TextField()
    estado=models.CharField(max_length=100) 
    disponible=models.BooleanField(default=True)

    id_libro=models.BigAutoField(primary_key=True)
    duenio=models.ForeignKey("Usuario",on_delete=models.SET_NULL,null=True,blank=True,related_name="libros")
    categoria=models.ForeignKey("Categoria",on_delete=models.PROTECT, related_name="libros")  #Tambien le podrias poner models.SET_NULL  
    
    genero=models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    