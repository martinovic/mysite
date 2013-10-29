# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-10-28"

from django.conf.urls import patterns, url

from principal import views
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^validate/$', views.validate, name='validate'),
)
