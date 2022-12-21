from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'posts'

urlpatterns = [
    path('create-post/', views.create_post, name='create_post'),
    path('post-detail/<str:id>/', views.post_detail, name='post_detail'),
    path('user-posts/', views.current_user_posts, name='current_user_posts'),
    path('<uuid:post>/like', views.post_like, name='like'),
    path('post/<str:id>/delete/', views.post_delete, name='post-delete'),
    ]
    