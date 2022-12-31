"""
A module for urls
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.urls import path
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
    ]
