from django.conf.urls import include, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from smarturls import surl

# Uncomment the next two lines to enable the admin:
admin.autodiscover()


urlpatterns = patterns('',
    surl('/', include('principal.urls', namespace="principal")),
    surl('/agenda/', include('agenda.urls', namespace="agenda")),
    surl('/cliente/', include('cliente.urls', namespace="cliente")),
    surl('/productos/', include('productos.urls', namespace="productos")),
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

    surl('/cliente/append_cliente/', 'cliente.views.append_cliente'),
    surl('/cliente/save_cliente/', 'cliente.views.save'),
)


urlpatterns += staticfiles_urlpatterns()
