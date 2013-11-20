# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-11-20"

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


def loginShow(request):
    '''Prueba de index'''
    return render(request, 'login.html')


def validate(request):
    '''valida el usuario'''
    c = {}
    c.update(csrf(request))
    context = {}

    username = request.POST["user"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/agenda/")
    else:
        context = {'message': 'Usuario no valido.'}
        return HttpResponseRedirect('/', context)


def logoutSystem(request):
    '''Sale del sistema y cierra la session'''
    logout(request)
    return HttpResponseRedirect('/')