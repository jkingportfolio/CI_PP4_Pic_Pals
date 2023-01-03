"""
A module for views of the contact app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.contrib import messages
# Internal
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def contact(request):
    """
    A function based view for the contact page with form to get
    contact details and reason for contacting
    """
    contact_form = ContactForm()
    form_submit = False
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for your message!')
            form_submit = True
            context = {
                'contact_form': contact_form,
                'form_submit': form_submit
            }
            return render(request, 'contact/contact_success.html', context)
    else:
        contact_form = ContactForm()
        context = {
                'contact_form': contact_form,
            }
    return render(request, 'contact/contact.html', context)
