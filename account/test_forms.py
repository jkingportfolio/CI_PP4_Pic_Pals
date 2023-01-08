# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# Internal:
from .models import Profile
from .forms import LoginDetails, Registration, EditUser
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestAccountForms(TestCase):
    """
    A class for testing contact forms
    """

    def setUp(self):
        """
        Create test user & profile
         """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password'
            )

        Profile.objects.create(user=test_user)

    def tearDown(self):
        """
        Delete test user
        """
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_login_form(self):
        """
        This test tests the login form
        """
        form = LoginDetails({
            'username': 'test_user',
            'password': 'test_password',
        })
        self.assertTrue(form.is_valid())

    def test_register_form(self):
        """
        This test tests the login form
        """
        form = Registration({
            'username': 'test_user1',
            'first_name': 'Mr Test',
            'email': 'test_user@email.com',
            'password': 'test_password',
            'password_confirm': 'test_password',
        })
        self.assertTrue(form.is_valid())

    def test_edit_user_form(self):
        """
        This test tests the login form
        """
        form = EditUser({
            'first_name': 'Tester',
            'last_name': 'Smith',
            'email': 'test_user@email.com'
        })
        self.assertTrue(form.is_valid())
