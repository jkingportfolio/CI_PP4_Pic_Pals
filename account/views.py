from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginDetails
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
