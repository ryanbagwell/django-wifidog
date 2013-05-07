import unittest
import urlparse
from django.core.urlresolvers import reverse
from django.test.client import Client
from .utilities import TokenMixin
from django.contrib.auth.models import User
from .models import *
from django.test.utils import override_settings


class WIFITest(TokenMixin, unittest.TestCase):
    test_username = 'john';
    test_user_email = 'johnsmith@gmail.com'
    test_user_password = 'testing123'


    def setUp(self):

        #create a fake test user to authenticate against
        try:
            self.user = User.objects.get(username=self.test_username)
        except:
            self.user = User.objects.create_user(self.test_username,
                self.test_user_email, self.test_user_password)


    def test_wifidog_ping(self):

        params = {
            'gw_id':'001217DA42D2',
            'sys_uptime':742725,
            'sys_memfree':2604,
            'sys_load':0.03,
            'wifidog_uptime':3861,
        }

        c = Client()

        r = c.get(reverse('wifi-ping'), params)

        """ Check for a 200 response code """
        self.assertEqual(r.status_code, 200)

        """ Check for the correct body response """
        self.assertEqual(r.content, 'Pong')

        """ Check if the ping object was properly saved to the db """
        ping_count = WIFIPing.objects.filter(**params).count()
        self.assertEqual(ping_count, 1)


    @override_settings(DEBUG=True)
    def test_login_success(self):

        c = Client()

        params = {
            'gw_id':'test-gw',
            'gw_address': '192.168.50.1',
            'gw_port': '2062',
            'url': 'http://www.google.com',
            'email': self.test_user_email,
            'password': self.test_user_password,
        }


        r = c.post(reverse('wifi-login'), params)

        """ a successful login will return a 302 redirect
            to the gateway """
        self.assertEqual(r.status_code, 302,
            msg="Found invalid status code. Should be 302.")

        """ Check that the token is valid """
        token = self.extract_token(url=r['location'])

        self.assertTrue(self.verify_token(token),
            msg="Could not verify token (%s)" % token)

        valid_redirect_url = 'http://%s:%s/wifidog/auth?token=%s' % (params['gw_address'], params['gw_port'], token)

        """ Check that the redirect url is correct """
        self.assertEqual(r['location'], valid_redirect_url,
            msg="Invalid redirect URL (%s). Found %s" % (valid_redirect_url,
            r['location']))

        """ Check that there's a valid token for the user """
        tokens = Token.objects.filter(token=token, user__email=params['email']).count()
        self.assertEqual(tokens, 1,
            msg="Found %s token(s) for logged-in user" % tokens)


    @override_settings(DEBUG=True)
    def test_login_failure(self):

        params = {
            'gw_id':'test-gw',
            'gw_address': '192.168.50.1',
            'gw_port': '2062',
            'url': 'http://www.google.com',
            'email': 'baduser@gmail.com',
            'password': self.test_user_password,
        }

        c = Client()
        r = c.post(reverse('wifi-login'), params)

        self.assertEqual(r.status_code, 200,
            msg="Login request returned a bad status code (%s). Should be 200." % r.status_code)


    @override_settings(DEBUG=True)
    def test_gateway_login_request_success(self):

        self.test_login_success()

        token_obj = Token.objects.filter(
            user__username=self.test_username)[0]

        params = {
            'stage':'login', #can be 'counters' or 'login'
            'ip': '192.168.50.13',
            'mac': 'e0:f8:47:30:ae:b4',
            'token': token_obj.token,
            'incoming': '6031353',
            'outgoing': '827770'
        }

        c = Client()

        r = c.get(reverse('wifi-auth'), params)

        self.assertEqual(r.status_code, 200,
            msg="Login request returned a bad status code (%s). Should be 200." % r.status_code)

        self.assertEqual(r.content, 'Auth: 1',
            msg="The server returned an invalid authorization response (%s). Expected: Auth: 1" % r.content)

        auth_requests = WIFIAuthRequest.objects.filter(token=token_obj.token, result=1).count()

        self.assertEqual(auth_requests, 1)


    @override_settings(DEBUG=True)
    def test_gateway_login_request_invalid(self):

        test_token = ':'.join([self.create_token().split(':')[0], '46ea0d5b246d2841744c26f72a86fc29'])

        params = {
            'stage':'login', #can be 'counters' or 'login'
            'ip': '192.168.50.13',
            'mac': 'e0:f8:47:30:ae:b4',
            'token': test_token,
            'incoming': '6031353',
            'outgoing': '827770'
        }

        c = Client()
        r = c.get(reverse('wifi-auth'), params)

        self.assertEqual(r.status_code, 200,
            msg="Login request returned a bad status code (%s). Should be 200." % r.status_code)

        self.assertEqual(r.content, 'Auth: 0',
            msg="The server returned an invalid authorization response (%s). Expected: Auth: 0" % r.content)

        WIFIAuthRequest.objects.get(token=test_token, result=0)














