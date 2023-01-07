# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestContactForms(TestCase):
    """
    A class for testing contact forms
    """
    def test_contact_form(self):
        """
        This test tests the contact form object
        """
        form = ContactForm({
            'reason': 'General',
            'name': 'tester',
            'email': 'test_user@test.com',
            'message': 'This is a test message',
            })
        self.assertTrue(form.is_valid())
