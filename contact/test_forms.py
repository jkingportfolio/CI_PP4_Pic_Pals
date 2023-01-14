"""
A module for testing forms in the contact app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# Internal:
from .models import Contact
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestContactForm(TestCase):
    """
    A class to test ContactForm
    """
    def test_empty_form(self):
        """
        To test empty form
        """
        form = ContactForm()
        self.assertIn("name", form.fields)
        self.assertIn("email", form.fields)
