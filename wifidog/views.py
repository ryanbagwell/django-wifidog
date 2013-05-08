from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib.auth.models import User
from .forms import LoginForm
from .utilities import TokenMixin
import logging




class BaseView(View):

    def post(self, request, *args, **kwargs):
        return HttpResponse('Invalid request.')


class WIFIPingView(BaseView):
    """ This handles the ping request from
        the router """

    def get(self, request, *args, **kwargs):

        try:
            m = WIFIPing(**request.GET.dict())
            m.save()
            return HttpResponse('Pong')
        except:
            return HttpResponse('Error')



class WIFIAuthView(TokenMixin, BaseView):
    """ This handles the request from the router client
        to report the status of each user connection.

        Must return one of the following codes:

        0 - AUTH_DENIED
        6 - AUTH_VALIDATION_FAILED
        1 - AUTH_ALLOWED
        5 - AUTH_VALIDATION
        -1 - AUTH_ERROR

        """


    def get(self, request, *args, **kwargs):

        token = self.extract_token(request=request)

        auth_request = WIFIAuthRequest(
            stage=request.GET.get('stage', None),
            ip=request.GET.get('ip', None),
            token=request.GET.get('token', None),
            incoming=request.GET.get('incoming', 0),
            mac=request.GET.get('mac', ''),
            outgoing=request.GET.get('outgoing', 0),)

        valid = self.is_token_valid(token)

        if valid:
            auth_request.result = 1
            auth_request.save()
            return HttpResponse('Auth: 1')

        else:
            auth_request.result = 0
            auth_request.save()
            return HttpResponse('Auth: 0')


    def is_token_valid(self, token):

        try:
            token_obj = Token.objects.get(token=token)
        except:
            return False

        if token_obj.is_valid():
            return True
        else:
            return False



class WIFILoginView(TokenMixin, FormView):
    template_name="wifidog/login.html"
    form_class = LoginForm

    """ The request to the login page """

    def get_initial(self):
        return self.request.GET.dict()


    def get_context_data(self, *args, **kwargs):

        context = super(WIFILoginView, self).get_context_data(**kwargs)

        if self.request.GET:
            context.update(**self.request.GET.dict())

        return context


    def get_success_url(self):

        return "http://%s:%s/wifidog/auth?token=%s" % (
            self.form.cleaned_data['gw_address'],
            self.form.cleaned_data['gw_port'],
            self.token)


    def form_valid(self, form):

        self.form = form

        """ Check if the person is authorized to log in. """

        success, user = self.authenticate(form.cleaned_data['email'],
            form.cleaned_data['password'])

        if not success:

            context = super(WIFILoginView, self).get_context_data()

            context.update({
                'invalid': True,
                'form': form,
                'invalid_message': "Invalid login. Please try again."
            })

            logging.getLogger('default').warn('Invalid login from %s' % form.cleaned_data['email'])

            return self.render_to_response(context)

        self.token = self.create_token()

        token_obj = Token(
            user=user,
            token=self.create_token(),
            ).save()

        return super(WIFILoginView, self).form_valid(form)


    def authenticate(self, email, password):

        if self.request.user.is_authenticated():
            return True, self.request.user

        try:
            user = User.objects.get(email=email)
        except:
            return (False, None)

        user = authenticate(username=user.username,
            password=password)

        if user is not None:

            if user.is_active:
                login(self.request, user)
                return True, user

            return False, user

        else:
            return False, user











