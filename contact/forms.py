from django import forms
from .models import Contact

 
class ContactForm(forms.ModelForm):
    """
    A class for the contact form
    """
    class Meta:
        model = Contact
        fields = ['reason', 'name', 'email', 'message']