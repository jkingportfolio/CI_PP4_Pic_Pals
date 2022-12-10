from django import forms


class LoginDetails(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
