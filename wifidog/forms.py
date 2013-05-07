from django import forms
from django.conf import settings


class WifidogField(forms.CharField):

    def __init__(self, *args, **kwargs):
        super(WifidogField, self).__init__(widget=forms.HiddenInput,
            required=False, *args, **kwargs)



class LoginForm(forms.Form):
    email = forms.EmailField(required=True,
        label='E-mail', error_messages={'required':'An E-mail is required'})
    password = forms.CharField(required=True,
        label='Password', widget=forms.PasswordInput(), error_messages={'required':'A password is required'})
    gw_address = WifidogField()
    gw_port = WifidogField()
    gw_id = WifidogField()
    url = WifidogField()

