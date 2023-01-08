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


class TestProfileViews(TestCase):

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

    def test_correct(self):
        test_user = authenticate(username='test_user', password='test_password')
        self.assertTrue((test_user is not None) and test_user.is_authenticated)

    def test_wrong_username(self):
        test_user = authenticate(username='wrong_user', password='test_password')
        self.assertFalse(test_user is not None and test_user.is_authenticated)

    def test_wrong_pssword(self):
        test_user = authenticate(username='test_user', password='wrong_password')
        self.assertFalse(test_user is not None and test_user.is_authenticated)
