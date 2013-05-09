from tastypie.serializers import Serializer
from django.utils import simplejson
from django.core.serializers import json



class SystemSatusSerializer(Serializer):

    def to_json(self, data, options=None):

        latest = data['objects'][0].data

        del latest['id']
        del latest['resource_uri']

        data = self.to_simple(latest, options)

        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True)