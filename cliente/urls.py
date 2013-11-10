# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'edgard pimentel'
__email__ = 'pimentelrojas@gmail.com'
__url__ = ''
__date__ = "2013-11-08"
__updated__ = "2013-11-08"

from django.conf.urls import patterns
from cliente import views

from smarturls import surl

urlpatterns = patterns('',
    surl('^$', views.index_cliente, name='index_cliente'),
)
