"""
A module for forms in the account app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Internal
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LoginDetails(forms.Form):
    """
    A class for a login details
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class Registration(UserCreationForm):
    """
    A class for a registering
    """
    first_name = forms.CharField(
        max_length=30, required=False)
    email = forms.EmailField(
        max_length=254)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
        ]


class EditUser(forms.ModelForm):
    """
    A class for updating user details from the built in Django model
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfile(forms.ModelForm):
    """
    A class for updating user profile details
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = forms.DateInput(
            attrs={'placeholder': 'MM/DD/YYYY'})
        self.fields['bio'].widget = forms.TextInput(
            attrs={'placeholder': 'Write a little about yourself.'})

    class Meta:
        model = Profile
        fields = ['profile_pic', 'date_of_birth', 'bio']
