"""
A module for testing views of the contact app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# Internal
from contact.models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestContactModel(TestCase):
    """
    A class for testing contact views
    """
    def setUp(self):
        """
        Create test user and contact categories
        """
        User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@email.com')
        
        Contact.objects.create(
            reason='test_reason',
            name='test_name',
            email='test@email,.com',
            message_body='test_message',
            message_date='01/01/2022'
        )

    def tearDown(self):
        """
        Delete test user and contact message
        """
        Contact.objects.all().delete()

    def test_contact_message(self):
        contact = Contact.objects.get(reason='test_name')
        self.assertEqual((contact.__str__()), contact.name)
