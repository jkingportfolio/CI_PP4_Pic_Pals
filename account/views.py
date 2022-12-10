from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginDetails

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginDetails(request.Post)
        if form.is_valid():
            clearform = form.cleaned_data
            user = authenticate(request,
            username = clearform['username'],
            password = clearnform['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(('Login authenticated'))
            else:
                return HttpResponse(('Account disabled'))
        else:
            return(HttpResponse('Invalid login'))
    else:
        form = LoginDetais()
    return render(request, 'account/login.html', {'form': form})

        
