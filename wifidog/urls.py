from django.conf.urls.defaults import *
from .views import *
from django.http import HttpResponseRedirect
from .api import SystemStatusResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(SystemStatusResource())


urlpatterns = patterns('',

    url(r'^ping/$', WIFIPingView.as_view(),
        name='wifi-ping'),

    url(r'^auth/(index\.php)?', WIFIAuthView.as_view(),
        name='wifi-auth'),

    url(r'^login/$', WIFILoginView.as_view(),
        name='wifi-login'),

    url(r'^portal/$', lambda x: HttpResponseRedirect('/'),
        name='wifi-portal'),

    url(r'^api/', include(v1_api.urls),
        name='wifidog-api-v1'),

)

