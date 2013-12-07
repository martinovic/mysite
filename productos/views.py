# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-11-20"

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render
from productos.models import Products


def index_product(request):
    '''Pagina indice'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    datos = Products.objects.order_by('name').all()
    context = {'posts': datos}
    return render(request, 'productos/index_productos.html', context)


def append_product(request):
    '''Agrega un producto'''
    c = {}
    c.update(csrf(request))
    context = {}
    if request.method == 'POST':
        if request.POST['id'] != 'none':
            datos = Products.objects.get(pk=int(request.POST['id']))
            context = {'posts': datos}
    return render(request, 'productos/append_producto.html', context)


def save_product(request):
    '''Graba un producto'''
    pass


def delete_product(request):
    '''Borra un producto'''
    pass


def search_product(request):
    '''Busqueda de un producto'''
    pass
