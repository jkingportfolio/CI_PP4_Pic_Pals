"""
A module for forms
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django import forms
# Internal
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactForm(forms.ModelForm):
    """
    A class for the contact form
    """
    class Meta:
        model = Contact
        fields = ['reason', 'name', 'email', 'message_body']