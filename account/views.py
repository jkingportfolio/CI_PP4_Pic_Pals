from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginDetails, Registration, Profile, EditUser, EditProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


# User login view
def user_login(request):
    if request.method == 'POST':
        form = LoginDetails(request.POST)
        if form.is_valid():
            clearform = form.cleaned_data
            user = authenticate(request, username=clearform['username'], password=clearform['password'])
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


# Logged in user dashboard view  
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': dashboard})


# User registration view
def register(request):
    if request.method == 'POST':
        user_form = Registration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_success.html', {'new_user': new_user})
    else:
        user_form = Registration()
    return render(request, 'account/register.html', {'user_form': user_form})


# Edit user profile view
@login_required()
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUser(instance=requesat.user, data=request.POST)
        profile_form = EditProfile(instance=request.user.profile, data=request.POST, files=reguest.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=request.user)
    return render(request, 'account/edit-profile.html', {'user_form': user_form, 'profile_form': profile_form})
