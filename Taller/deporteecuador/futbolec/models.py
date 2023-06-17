from django.db import models

# Create your models here.

class Equipof(models.Model):


    nombre = models.CharField('Nombre del equipo',max_length=40)
    siglas = models.CharField(max_length=30)
    tusername = models.CharField('Usario de twitter', max_length=30)

class Jugador(models.Model):
    
    nombre = models.CharField('Nombre Jugador', max_length=40)
    posicion = models.CharField(max_length=50)
    camiseta = models.ImageField('Numero de camiseta')
    sueldo = models.DecimalField()
    
    equipo = models.ForeignKey(Equipof, on_delete=models.CASCADE, related_name= "equipo_futbol")

class Campeonato(models.Model):

    nombre = models.CharField('Nombre del campeonato', max_length=50)
    nombreausp = models.CharField('Nombre del auspiciante', max_length=50)


class Campeonato_equipo:

    año = models.IntegerField()
    