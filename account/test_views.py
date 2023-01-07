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


class TestAccountViews(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and test user profile
         """
        testuser = User.objects.create_user(
            username = 'test_user',
            password = 'test_password',
            email = 'test_user@test.com')
        testuser.save()

        Profile.objects.create(
            user = Profile.objects.get(user=testuser),
            date_of_birth = '01/01/2023',
            profile_pic = 'test_user@test.com',
            bio = '12345678',
        )

    def tearDown(self):
        """
        Delete test user and Profile
        """
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_get_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (get) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)

