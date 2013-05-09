from django.contrib import admin
from .models import *

class WIFIPingAdmin(admin.ModelAdmin):
    readonly_fields = ['gw_id', 'sys_uptime', 'sys_memfree', 'wifidog_uptime', 'sys_load']

    list_display = ['gw_id', 'sys_uptime', 'sys_memfree', 'wifidog_uptime', 'sys_load', 'ping_time',]


admin.site.register(WIFIPing, WIFIPingAdmin)


class WIFIAuthRequestAdmin(admin.ModelAdmin):

    readonly_fields = ['user', 'stage', 'ip', 'mac', 'token', 'incoming', 'incoming_use', 'outgoing', 'outgoing_use', 'result', 'request_time']

    list_display = ['user', 'stage', 'ip', 'mac', 'token', 'incoming', 'incoming_use', 'outgoing', 'outgoing_use', 'result', 'request_time']

    ordering = ['-request_time']

admin.site.register(WIFIAuthRequest, WIFIAuthRequestAdmin)


class TokenAdmin(admin.ModelAdmin):

    readonly_fields = ['user', 'token', 'created', 'expires']

    list_display = ['user', 'token', 'created', 'expires']

    ordering = ['-created']

admin.site.register(Token, TokenAdmin)