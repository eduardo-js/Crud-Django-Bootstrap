# -*- coding: utf-8 -*-

from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    ano = models.IntegerField()
    Km = models.FloatField()
