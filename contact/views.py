from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    contact_form = ContactForm()
    form_submit = False
    if request.method == 'GET':
        if not request.user.is_authenticated:
            contact_form = ContactForm()
        elif request.user.profile:
            contact_form = ContactForm(
                initial={
                    'name': request.user.first_name,
                    'email': request.user.email,
                }
            )
        else:
            contact_form = ContactForm()
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
        contact_form = ContactForm(initial={
                    'name': request.user.first_name,
                    'email': request.user.email,
                }
            )
        context = {
                'contact_form': contact_form,
            }
    return render(request, 'contact/contact.html', context)

