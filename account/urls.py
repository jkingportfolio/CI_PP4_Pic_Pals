"""
A module for urls
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.urls import path, include
from django.contrib.auth import views as auth_views
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    # Using djangos prefab authentication views
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#all-authentication-views
    path('login/', auth_views.LoginView.as_view(),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('edit-profile/', views.edit_profile,
         name='edit_profile'),
    path('users/', views.site_users,
         name='site_users'),
    path('users/search/', views.search_users,
         name='search_users'),
    path('users/<username>/', views.user_detail,
         name='user_detail'),
    path('follow-user/<str:user_name>/', views.follow_user,
         name='follow_user'),
    path('users/<username>/following/', views.following_list,
         name='following_list'),
    path('users/<username>/followers/', views.follower_list,
         name='followers_list'),
]
