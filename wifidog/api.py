from tastypie.resources import ModelResource
from .models import *
from .serializers import *
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from django.contrib.auth.models import User


class SystemStatusResource(ModelResource):

    class Meta:
        queryset = WIFIPing.objects.order_by('-ping_time')[:2]
        resource_name = 'status'
        serializer = SystemSatusSerializer()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()


class UserStatusResource(ModelResource):

    class Meta:
        queryset = WIFIAuthRequest.objects.all()
        resource_name = 'status'
        serializer = SystemSatusSerializer()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()