# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
# Internal
from .models import Profile, Follow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PASSES


class TestAccountModels(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and test user profile
         """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com'
        )

    def tearDown(self):
        """
        Delete test user and Profile
        """
        User.objects.all().delete()

    def test_profile_str_method(self):
        """
        This test tests the users profile
        """
        test_user = User.objects.get(username='test_user')
        profile = Profile.objects.create(user=test_user)
        self.assertEqual(str(profile), f'Profile of {profile.user.username}')

