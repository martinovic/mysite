from django.conf.urls import patterns, include    # , url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# amitu.com/smarturls
from smarturls import surl


urlpatterns = patterns('',
    surl('/', include('polls.urls', namespace="polls")),
    surl('/login/', include('principal.urls', namespace="principal")),
    surl('/agenda/', include('agenda.urls', namespace="agenda")),
    surl('/polls/', include('polls.urls', namespace="polls")),
    surl('/developers/', include('developers.urls', namespace="developers")),
    surl('/recover_password/', include('recover_password.urls', namespace="recover_password")),
    surl('/admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
