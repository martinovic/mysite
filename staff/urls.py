# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-11-22"
__updated__ = "2013-11-26"

from django.conf.urls import patterns, url

from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     url(r'^(?P<poll_id>\d+)/verPost/$', views.verPost, name='verPost'),
)