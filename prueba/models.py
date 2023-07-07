from django.db import models

# Create your models here.
class Seccion(models.Model):
    seccion = models.CharField(max_length=10)

class Plantas(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.nombre
    
class Macetas(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.nombre
    
class Tierras(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True)

    def __str__(self):
        return self.nombre