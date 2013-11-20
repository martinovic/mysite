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
from agenda.models import Diary


def index_agenda(request):
    '''Index Page'''
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")

    datos = Diary.objects.order_by('razonNombreApellido').all()
    context = {'posts': datos}
    return render(request, 'agenda/index_agenda.html', context)


def append_agenda(request):
    '''Append to agenda'''
    c = {}
    c.update(csrf(request))
    context = {}
    if request.method == 'POST':
        if request.POST['id'] != 'none':
            datos = Diary.objects.get(pk=int(request.POST['id']))
            context = {'posts': datos}
    return render(request, 'agenda/append_agenda.html', context)


def save_agenda(request):
    '''Graba los datos'''
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        razonNombreApellido = request.POST['razonNombreApellido']
        calle = request.POST['calle']
        numero = request.POST['numero']
        piso = request.POST['piso']
        ciudad = request.POST['ciudad']
        provincia = request.POST['provincia']
        pais = request.POST['pais']
        telefono1 = request.POST['telefono1']
        telefono2 = request.POST['telefono2']
        telefono3 = request.POST['telefono3']
        telefono4 = request.POST['telefono4']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        email3 = request.POST['email3']
        tipoEntrada = request.POST['tipoEntrada']
        productos = request.POST['productos']
        pago = request.POST['pago']
        cuit = request.POST['cuit']
        cbu = request.POST['cbu']
        banco = request.POST['banco']
        horario = request.POST['horario']
        observaciones = request.POST['observaciones']
        transportes = request.POST['transportes']
        if request.POST['id'] != "":
            agendaSave = Diary.objects.get(pk=request.POST['id'])
            agendaSave.razonNombreApellido = razonNombreApellido
            agendaSave.calle = calle
            agendaSave.numero = numero
            agendaSave.piso = piso
            agendaSave.ciudad = ciudad
            agendaSave.provincia = provincia
            agendaSave.pais = pais
            agendaSave.telefono1 = telefono1
            agendaSave.telefono2 = telefono2
            agendaSave.telefono3 = telefono3
            agendaSave.telefono4 = telefono4
            agendaSave.email1 = email1
            agendaSave.email2 = email2
            agendaSave.email3 = email3
            agendaSave.tipoEntrada = tipoEntrada
            agendaSave.productos = productos
            agendaSave.pago = pago
            agendaSave.cuit = cuit
            agendaSave.banco = banco
            agendaSave.cbu = cbu
            agendaSave.horario = horario
            agendaSave.observaciones = observaciones
            agendaSave.transportes = transportes
        else:
            agendaSave = Diary(razonNombreApellido=razonNombreApellido,
                calle=calle, numero=numero,
                piso=piso, ciudad=ciudad,
                provincia=provincia, pais=pais,
                telefono1=telefono1, telefono2=telefono2,
                telefono3=telefono3, telefono4=telefono4,
                email1=email1, email2=email2, email3=email3,
                tipoEntrada=tipoEntrada, productos=productos,
                pago=pago, cuit=cuit, banco=banco, transportes=transportes,
                cbu=cbu, horario=horario, observaciones=observaciones)
        try:
            agendaSave.save()
            return render(request, 'agenda/save_agenda.html')
        except:
            return render(request, 'agenda/failsave_agenda.html')


def delete_agenda(request):
    '''Borrado de datos'''
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        try:
            Diary.objects.get(pk=request.POST['id']).delete()
            context = {'message': 'Se ha borrado el registro.'}
            return render(request, 'agenda/delete_agenda.html', context)
        except:
            context = {'error_message': 'No se pudo borrar el archivo'}
            return render(request, 'agenda/delete_agenda.html', context)


def search_agenda(request):
    '''Busqueda de datos'''
    c = {}
    c.update(csrf(request))
    print(request.POST["s"])
    try:
        datos = get_object_or_404(Diary,
            razonNombreApellido__contains=request.POST["s"])
        context = {'posts': datos}
    except:
        context = {'error_message': 'Dato no encontrado'}

    return render(request, 'agenda/search_agenda.html', context)
