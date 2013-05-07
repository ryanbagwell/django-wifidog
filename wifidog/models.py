from django.db import models
from django.contrib.auth.models import User
import time, datetime

class WIFIPing(models.Model):
    gw_id = models.CharField(max_length=255)
    sys_uptime = models.IntegerField()
    sys_memfree = models.IntegerField()
    wifidog_uptime = models.IntegerField()
    sys_load = models.FloatField()
    ping_time = models.DateTimeField(auto_now=True, auto_now_add=True)


class WIFIAuthRequest(models.Model):
    user = models.ForeignKey(User, related_name='auth_requests', blank=True, null=True)
    stage = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    incoming = models.IntegerField()
    outgoing = models.IntegerField()
    result = models.IntegerField(default=0)
    request_time = models.DateTimeField(auto_now=True,
        auto_now_add=True)

    def save(self, *args, **kwargs):

        try:
            token = Token.objects.get(token=self.token)
            self.user = token.user
        except:
            pass

        super(WIFIAuthRequest, self).save(*args, **kwargs)


class Token(models.Model):
    user = models.ForeignKey(User, related_name='tokens', primary_key=True)
    token = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    expires = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if self.expires is None:
            self.expires = datetime.datetime.now() + datetime.timedelta(1,0)


        super(Token, self).save(*args, **kwargs)


    def is_valid(self):

        if self.user.is_active == False:
            print "Invalid user"
            return False

        if self.expires < datetime.datetime.now():
            print "Expired token"
            return False

        return True










