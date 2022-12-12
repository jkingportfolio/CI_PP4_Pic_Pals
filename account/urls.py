from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Using djangos prefab authentication views
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#all-authentication-views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]
