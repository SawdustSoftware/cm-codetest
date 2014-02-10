""" Test all views regarding account registration/authorization"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

class AuthorizationViewTest(TestCase):
    """ Test views with regard to authorization"""

    def setUp(self):
        """Set up database and client"""
        get_user_model().objects.create_user(username='test', password='asdf')
        self.client = Client()

    def test_logout(self):
        """ Verify logout url logs out a client """
        self.assertTrue(self.client.login(username='test', password='asdf'))

        # Check to see if client is redirected accordingly
        response = self.client.get(reverse('accounts:logout'))


        # Verify they are logged out
        self.assertNotIn('_auth_user_id', self.client.session)


