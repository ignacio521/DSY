from django.db import models


class Administrador(models.Model):
    id_ad= models.AutoField(primary_key = True)
    nombre_completo_ad= models.CharField('nombre_completo_ad', max_length = 200, blank = False, null = False)
    nombre_usuario_ad = models.CharField('nombre_usuario_ad', max_length = 220, blank = False, null = False)
    Estado_actual = models.CharField('Estado_actual', max_length = 220, blank = False, null = False)
    contrasena_ad= models.CharField('contrasena_ad', max_length = 220, blank = False, null = False)

	





class Usuario(models.Model):
    id_us = models.AutoField(primary_key = True)
    nombre_completo_us= models.CharField('nombre_completo_us', max_length = 200, blank = False, null = False)
    nombre_usuario_us = models.CharField('nombre_usuario_us', max_length = 200, blank = False, null = False)
    contrasena_us= models.CharField('contrasena_us', max_length = 220, blank = False, null = False)





class Equipo(models.Model):
    id_eq = models.AutoField(primary_key = True)
    nombre_equipo= models.CharField('nombre_equipo', max_length = 200, blank = False, null = False)
    pokemon_1 = models.CharField('pokemon_1', max_length = 200, blank = False, null = False)
    pokemon_2 = models.CharField('pokemon_2', max_length = 200, blank = False, null = False)
    pokemon_3 = models.CharField('pokemon_3', max_length = 200, blank = False, null = False)
    pokemon_4 = models.CharField('pokemon_4', max_length = 200, blank = False, null = False)
    pokemon_5 = models.CharField('pokemon_5', max_length = 200, blank = False, null = False)
    pokemon_6 = models.CharField('pokemon_6', max_length = 200, blank = False, null = False)



