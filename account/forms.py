from django import forms
from django.contrib.auth.models import User


class LoginDetails(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class Registration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def reset_password_confirm(self):
        clear = self.cleaned_data
        if clear['password'] != clear['password_confirm']:
            raise forms.ValidationError('Password re entry does not match.')
        return clear['password_confirm']
