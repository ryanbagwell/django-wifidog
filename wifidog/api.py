from tastypie.resources import ModelResource
from .models import *
from .serializers import *


class SystemStatusResource(ModelResource):

    class Meta:
        queryset = WIFIPing.objects.order_by('-ping_time')[:2]
        resource_name = 'status'
        serializer = SystemSatusSerializer()