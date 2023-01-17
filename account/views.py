"""
A module for views in the account app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, View
# Internal
from .models import Profile, Follow
from .forms import (LoginDetails,
                    Registration,
                    Profile,
                    EditUser,
                    EditProfile)
from post.models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class SignUpView(CreateView):
    """
    A class based view for the register page with
    a form to take the new users details
    """

    def get(self, request, *args, **kwargs):
        user_form = Registration()
        return render(request, 'account/register.html',
                      {'user_form': user_form})

    def post(self, request, *args, **kwargs):
        user_form = Registration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request, f'Welcome {new_user.username}!')
            context = {
                'new_user': new_user,
            }
            return render(request, 'account/register_success.html', context)
        else:
            user_form = Registration()
        return render(request, 'account/register.html',
                      {'user_form': user_form})


class RegisterSuccess(View):
    def get(self, request):
        new_user = get_object_or_404(Profile, user=request.user)
        messages.success(request, f'Welcome {new_user.username}!')
        context = {
            'new_user': new_user,
        }
        return render(request, 'account/register_success.html', context)


@login_required
def dashboard(request):
    """
    A function based view for the logged in users profile
    page with a list of their posts, button to add a post, account
    stats and options to update profile and change password
    """
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user = request.user
    user_posts = Post.objects.filter(user=user)
    user_posts_count = user_posts.count()
    user_followers_count = Follow.objects.filter(followed_account=user).count()
    user_following_count = Follow.objects.filter(user=user).count()
    context = {
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_posts_count': user_posts_count,
        'user_followers_count': user_followers_count,
        'user_following_count': user_following_count,
    }
    return render(request, 'account/dashboard.html', context)


@login_required()
def edit_profile(request):
    """
    A function based view for the edit profile page with form
    to input new profile details
    """
    if request.method == 'POST':
        user_form = EditUser(instance=request.user,
                             data=request.POST)
        profile_form = EditProfile(instance=request.user.profile,
                                   data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('/')
        else:
            messages.error(request, 'Error updating profile.')
    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=request.user.profile)
    return render(request, 'account/edit_profile.html',
                  {'user_form': user_form, 'profile_form': profile_form})


@login_required
def site_users(request):
    """
    A function based view for the people page which will return a list of
    all pic pals users and a search bar for the ability to search for users
    """
    users = User.objects.all().order_by('username')
    return render(request, 'account/user/user_list.html', {'users': users})


@login_required
def user_detail(request, username):
    """
    A fucntion based view for the user page of another user
    which will display all users posts, profile stat and the
    ability to follow the account
    """
    user = get_object_or_404(User, username=username, is_active=True)
    user_posts = Post.objects.filter(user=user)
    user_post_count = user_posts.count()
    user_followers = Follow.objects.filter(followed_account=user)
    user_followers_count = user_followers.count()
    user_following_list = Follow.objects.filter(user=user)
    user_following_count = Follow.objects.filter(user=user).count()
    user_followers_list = Follow.objects.filter(followed_account=user)
    user_follow_status = False
    if Follow.objects.filter(
            user=request.user, followed_account=user).exists():
        user_follow_status = True
    context = {
        'user': user,
        'user_posts': user_posts,
        'user_post_count': user_post_count,
        'user_followers': user_followers,
        'user_followers_count': user_followers_count,
        'user_followers_list': user_followers_list,
        'user_following_count': user_following_count,
        'user_follow_status': user_follow_status,
    }
    return render(request, 'account/user/user_detail.html', context)


@login_required
def follow_user(request, user_name):
    """
    A function based view to allow a user to follow and
    unfollow another pic pal user
    """
    user_to_follow = User.objects.get(username=user_name)
    current_user = request.user
    get_user = User.objects.get(username=current_user)
    follow_status, created = Follow.objects.get_or_create(
        user=get_user, followed_account=user_to_follow)
    if user_to_follow.username != current_user.username:
        if not created:
            follow_status.delete()
            messages.success(
                request, f'Unfollowed {user_to_follow} successfully')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(
                request, f'Followed {user_to_follow} successfully')
            return redirect(request.META.get('HTTP_REFERER'))


@login_required
def following_list(request, username):
    """
    A function based view for the following list page which will
    display a list of all users the current user follows
    """
    user = get_object_or_404(User, username=username, is_active=True)
    user_following_list = Follow.objects.filter(user=user)
    context = {
        'user': user,
        'user_following_list': user_following_list
    }
    return render(request, 'account/user/following_list.html', context)


@login_required
def follower_list(request, username):
    """
    A function based view for the follower list page which will
    display a list of all users the current user is followed by
    """
    user = get_object_or_404(User, username=username, is_active=True)
    user_followers_list = Follow.objects.filter(followed_account=user)
    context = {
        'user': user,
        'user_followers_list': user_followers_list
    }
    return render(request, 'account/user/followers_list.html', context)


@login_required
def search_users(request):
    """
    A function based view for the ability to search for users from
    the people page
    """
    query = request.GET.get('p')
    user_search_results = User.objects.filter(username__icontains=query)
    context = {
        'user_search_results': user_search_results,
    }

    return render(request, "account/user/user_search.html", context)
