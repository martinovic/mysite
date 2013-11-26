# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-10-29"


from django.db import models

from agenda.models import Diary


class Rubros(models.Model):
    '''Rubros'''
    rubro = models.CharField(max_lenght=150, blank=False, unique=True)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.rubro


class Stock(models.Model):
    '''Stock'''
    codigo = models.CharField(max_length=50, blank=False, unique=True)
    rubro = models.ForeignKey(Rubros)
    destalle = models.CharField(max_length=50, blank=False)
    cantidad = models.IntegerField(default=0)
    unidad = models.CharField(max_length=20, blank=True)
    precioCompra = models.FloatField(default=0)
    precioVenta = models.FloatField(default=0)
    ultimaFechaDeCompra = models.DateField(blank=False)
    ultimoProveedor = models.IntegerField(default=0, blank=False)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.codigo


class Historial(models.Model):
    '''Historial de compras'''
    fecha = models.DateField()
    codigo = models.ForeignKey(Stock)
    cantidad = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Diary)
    precioCompra = models.FloatField(default=0)
    factura = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.fecha
