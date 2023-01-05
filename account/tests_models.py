"""
A module for testing views of the account app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# Internal
from .models import Profile, Follow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProfileModels(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and test user profile
         """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        testuser.save()

    def tearDown(self):
        """
        Delete test user and Profile
        """
        User.objects.all().delete()

    def test_get_profile_page(self):
        """
        This test tests the users profile username
        """
        testuser = User.objects.get(username='test_user')
        profile = Profile.objects.create(user=testuser)
        self.assertEqual(str(profile), f'Profile of {profile.user.username}')
