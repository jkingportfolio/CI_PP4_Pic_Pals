from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginDetails, Registration, Profile, EditUser, EditProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Follow
from post.models import Post
from django.contrib import messages

# Create your views here.



"""
View to log in a user
"""
def user_login(request):
    if request.method == 'POST':
        form = LoginDetails(request.POST)
        if form.is_valid():
            clear_form = form.cleaned_data
            user = authenticate(request, username=clear_form['username'], password=clear_form['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(('Login authenticated'))
                else:
                    return HttpResponse(('Account disabled'))
            else:
                return (HttpResponse('Invalid login'))
    else:
        form = LoginDetails()
    return render(request, 'account/login.html', {'form': form})



"""
View to register an account
"""
def register(request):
    if request.method == 'POST':
        user_form = Registration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            print('account created')
            return render(request, 'account/register_success.html', {'new_user': new_user})
    else:
        user_form = Registration()
    return render(request, 'account/register.html', {'user_form': user_form})


"""
View of logged in users dashboard
""" 
@login_required
def dashboard(request):
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


"""
View to edit profile of logged in user
""" 
@login_required()
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUser(instance=request.user, data=request.POST)
        profile_form = EditProfile(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating profile.')
    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=request.user)
    return render(request, 'account/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


"""
View that returns all registered users
""" 
@login_required
def site_users(request):
    users = User.objects.all()
    return render(request, 'account/user/user_list.html', {'users': users})


"""
View to return all details of a user (viewing, not logged in as)
""" 
@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    print(f'user_detail user is: {user}')
    user_posts = Post.objects.filter(user=user)
    user_post_count = user_posts.count()
    user_followers = Follow.objects.filter(followed_account=user)
    user_followers_count = user_followers.count()
    user_following_count = Follow.objects.filter(user=user).count()
    user_following_list = Follow.objects.filter(user=user)
    print(f'This user is following users: {user_following_list}')
    print(f'This user follows {user_following_count} users.')
    print(f'This user has {user_followers_count} followers.')
    user_followers_list = Follow.objects.filter(followed_account=user)
    print(f'user_detail user_followers_list is: {user_followers_list}')
    try:
        user_follow_status = Follow.objects.filter(user=request.user, followed_account=user.username).exists()
    except Follow.DoesNotExist:
        user_follow_status = False
    print(user_follow_status)
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


"""
View to follow a user
""" 
@login_required
def follow_user(request, user_name):
    user_to_follow = User.objects.get(username=user_name)
    print(f'{request.user} Is away to follow: {user_to_follow}')
    current_user = request.user
    print(f'Logged in as: {current_user}')
    get_user = User.objects.get(username=current_user)
    print(f'Get user: {get_user}')
    follow_status, created = Follow.objects.get_or_create(user=get_user, followed_account=user_to_follow)
    if user_to_follow.username != current_user.username:
        if not created:
            print(follow_status)
            follow_status.delete()
            messages.success(request, 'Unfollowed added successfully')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, 'Follow added successfully')
            return redirect(request.META.get('HTTP_REFERER'))







