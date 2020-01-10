from django.db import models

# Create your models here.

class Clintes(models.Model):
    Codigo=models.IntegerField()
    Nombre=models.CharField(max_length=30)
    Direccion=models.CharField(max_length=50)
    Telefono=models.CharField(max_length=10)
    Saldo=models.IntegerField()
    UltimoAbono=models.DateField()
    Zona=models.CharField(max_length=45)



class Articulos(models.Model):
    Codigo=models.IntegerField()
    Nombre=models.CharField(max_length=30)
    Proveedor=models.CharField(max_length=30)




class Usuarios(models.Model):
    Cliente=models.CharField(max_length=20)
    Empresa=models.CharField(max_length=20)
    Estado=models.BooleanField()



class Zonas(models.Model):
    Codigo=models.IntegerField()
    Nombre=models.CharField(max_length=25)



class Vehiculos(models.Model):
    Codigo=models.IntegerField()
    Nombre=models.CharField(max_length=30)


class Empleados(models.Model):
    Codigo=models.IntegerField()
    Nombre=models.CharField(max_length=20)
    telefono=models.IntegerField()
    Direccion=models.CharField(max_length=30)


class Ventas(models.Model):
    Nombre=models.CharField(max_length=30)

    










    


