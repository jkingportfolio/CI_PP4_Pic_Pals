from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from .models import Profile

"""
A class for a login details
""" 
class LoginDetails(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

"""
A class for a password when registering
""" 
class Registration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='Password Confirm', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def reset_password_confirm(self):
        clear = self.cleaned_data
        if clear['password'] != clear['password_confirm']:
            raise forms.ValidationError('Password re entry does not match.')
        return clear['password_confirm']

 
"""
A class for updating user details from the built in Django model
""" 
class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


"""
A class for updating user profile details
""" 
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'dob', 'bio']
