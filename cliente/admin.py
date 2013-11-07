# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'edgard pimentel'
__email__ = 'pimentelrojas@gmail.com'
__url__ = ''
__date__ = "2013-11-06"
__updated__ = "2013-11-06"

from django.contrib import admin
from cliente.models import Cliente


admin.site.register(Cliente)
