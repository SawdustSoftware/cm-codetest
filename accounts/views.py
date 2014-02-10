"""All views dealing with accounts/authentication/authorization """

from django.views.generic import View
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse


class Logout(View):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))