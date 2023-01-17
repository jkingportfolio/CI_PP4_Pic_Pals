from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    messages.success(request, f'{user.username} successfully logged in!')


@receiver(user_logged_out)
def on_logout(sender, user, request, **kwargs):
    messages.success(request, f'{user.username} successfully logged out!')
