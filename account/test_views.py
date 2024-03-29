"""
A module for testing views in the account app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

# Internal:
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestAccountViews(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and test user profile
         """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
        )
        Profile.objects.create(user=test_user)

    def tearDown(self):
        """
        Delete test user and order
        """
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_correct_login(self):
        """
        This test tests the login form
        """
        test_user = authenticate(username='test_user',
                                 password='test_password')
        self.assertTrue((test_user is not None) and test_user.is_authenticated)

    def test_wrong_username(self):
        """
        This test tests a wrong username
        """
        test_user = authenticate(username='wrong_user',
                                 password='test_password')
        self.assertFalse(test_user is not None and test_user.is_authenticated)

    def test_wrong_password(self):
        """
        This test tests correct username and wrong password
        """
        test_user = authenticate(username='test_user',
                                 password='wrong_password')
        self.assertFalse(test_user is not None and test_user.is_authenticated)
