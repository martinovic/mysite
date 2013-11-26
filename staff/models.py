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


class Staff(models.Model):
    '''Empleados de las sucursales, nombre, legajo'''
    nombreApellido = models.CharField(max_length=200, blank=False)
    legajo = models.CharField(max_length=200, blank=False)
    fechaIngreso = models.DateField()

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.nombreApellido