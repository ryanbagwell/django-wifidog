import urlparse
from django.conf import settings
from django.core.signing import TimestampSigner


class TokenMixin(object):
    signer = None

    def verify_token(self, token):
        """ verifies the token """

        try:
            self._get_signer().unsign(token, max_age=60)
            return True
        except:
            return False


    def create_token(self):
        """ Generates a one-time use token based on
            a timestamp """

        return self._get_signer().sign(self._get_token_prefix())



    def extract_token(self, request=None, url=None):
        """ Extracts the 'token' param from a GET request. """

        if request is not None:
            return request.GET.get('token', None)

        return urlparse.parse_qs(
            urlparse.urlparse(url).query).get('token')[0]


    def _get_salt(self):

        return getattr(settings, 'AUTH_SALT',
            '0683fd711a3796825f1c0cbe3ab22443')

    def _get_token_prefix(self):

        return getattr(settings, 'WIFIDOG_TOKEN_PREFIX',
            'wifidog')

    def _get_signer(self):

        if self.signer is None:
            self.signer = TimestampSigner(salt=self._get_salt())

        return self.signer

