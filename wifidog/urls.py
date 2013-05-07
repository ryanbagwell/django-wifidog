from django.conf.urls.defaults import *
from .views import *
from django.http import HttpResponseRedirect


urlpatterns = patterns('',

    url(r'^ping/$', WIFIPingView.as_view(),
        name='wifi-ping'),

    url(r'^auth/(index\.php)?', WIFIAuthView.as_view(),
        name='wifi-auth'),

    url(r'^login/$', WIFILoginView.as_view(),
        name='wifi-login'),

    url(r'^portal/$', lambda x: HttpResponseRedirect('/'),
        name='wifi-portal'),

)

