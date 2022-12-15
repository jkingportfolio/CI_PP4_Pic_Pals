from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name='create_post'),
    path('post-detail/<int:id>/<slug:slug>/', views.post_detail, name='post_detail'),
]
