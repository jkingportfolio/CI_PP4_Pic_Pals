from . import views
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    # Using djangos prefab authentication views
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#all-authentication-views
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]