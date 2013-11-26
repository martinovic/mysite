# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-11-22"
__updated__ = "2013-11-26"

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render

from staff.models import Staff


def index_staff(request):
    '''Pagina indice'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    datos = Staff.objects.order_by('nombreApellido').all()
    context = {'posts': datos}
    return render(request, 'staff/index_staff.html', context)