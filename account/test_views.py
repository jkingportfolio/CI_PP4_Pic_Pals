# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
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

    def test_get_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (get) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)

    def test_post_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (post) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post('/account/')
        self.assertEqual(response.status_code, 200)