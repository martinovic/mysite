from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('polls.urls', namespace="polls")),
    url(r'^login/', include('principal.urls', namespace="principal")),
    url(r'^agenda/', include('agenda.urls', namespace="agenda")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^recover_password/', include('recover_password.urls', namespace="recover_password")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
