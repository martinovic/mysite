# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-11-20"
__updated__ = "2013-11-20"


from django.db import models


class Products(models.Model):
    '''Modelo de productos'''
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    created = models.DateField()
    updated = models.DateField(auto_now_add=True)
    category_id = models.IntegerField(default=0)
    enabled = models.BooleanField()

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.name


class Categories(models.Model):
    '''Modelo de categorias de productos'''
    name = models.CharField(max_length=200, blank=False)
    parent_id = models.ForeignKey(Products)
    typeCategorie = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.name
