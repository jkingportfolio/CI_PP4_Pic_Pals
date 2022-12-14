"""
A module for forms
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
# Internal
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LoginDetails(forms.Form):
    """
    A class for a login details
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class Registration(forms.ModelForm):
    """
    A class for a password when registering
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='Password Confirm',
                                       widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def reset_password_confirm(self):
        clear = self.cleaned_data
        if clear['password'] != clear['password_confirm']:
            raise forms.ValidationError('Password re entry does not match.')
        return clear['password_confirm']


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
        self.fields['date_of_birth'].widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'})
        self.fields['bio'].widget=forms.TextInput(attrs={'placeholder': 'Write a little about yourself.'})

    class Meta:
        model = Profile
        fields = ['profile_pic', 'date_of_birth', 'bio']
