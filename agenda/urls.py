# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-10-31"

from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from agenda import views
from agenda.models import Agenda

# amitu.com/smarturls
from smarturls import surl

urlpatterns = patterns('',
    surl('^$', views.index_agenda, name='index_agenda'),

#     surl('^append_agenda/$', views.append_agenda, name='append_agenda'),
#     surl('^save_agenda/$', views.save_agenda, name='save_agenda'),
#     surl('^search_agenda/$', views.search_agenda, name='search_agenda'),
#     surl('^delete_agenda/$', views.delete_agenda, name='delete_agenda'),

#     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     url(r'^(?P<poll_id>\d+)/verPost/$', views.verPost, name='verPost'),
)
