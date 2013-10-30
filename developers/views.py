# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-10-30"

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader, Context
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login


def index_developers(request):
    '''Indice que muestra los participantes del proyecto'''
    return render(request, 'index_developers.html')