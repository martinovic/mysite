# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-11-22"
__updated__ = "2013-11-26"

from django.db import models


class Stores(models.Model):
    '''Empleados del comercio, nombre, legajo'''
    sucursal = models.CharField(max_length=200, blank=False)
    calle = models.CharField(max_length=200, blank=False)
    numero = models.CharField(max_length=200, blank=False)
    telefono = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.sucursal