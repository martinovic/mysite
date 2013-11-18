from django.conf.urls import patterns, include  # , url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found
from django.views.defaults import permission_denied

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# amitu.com/smarturls
from smarturls import surl


# custom error pages
handler500 = curry(server_error, template_name='500.html')
handler404 = curry(page_not_found, template_name='404.html')
handler403 = curry(permission_denied, template_name='403.html')

urlpatterns = patterns('',
    surl('/', include('principal.urls', namespace="principal")),
    surl('/agenda/', include('agenda.urls', namespace="agenda")),
    surl('/cliente/', include('cliente.urls', namespace="cliente")),
    surl('/developers/', TemplateView.as_view(template_name='developers.html')),
    surl('/recover_password/',
        include('recover_password.urls', namespace="recover_password")),
    surl('admin/', include(admin.site.urls)),

    surl('/validate/', 'principal.views.validate'),
    surl('/logout/', 'principal.views.logoutSystem'),

    surl('/agenda/append_agenda/', 'agenda.views.append_agenda'),
    surl('/agenda/save_agenda/', 'agenda.views.save_agenda'),
    surl('/agenda/search_agenda/', 'agenda.views.search_agenda'),
    surl('/agenda/delete_agenda/', 'agenda.views.delete_agenda'),
)

urlpatterns += staticfiles_urlpatterns()
