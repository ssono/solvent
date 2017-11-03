from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    """should look like front page later"""
    return render(request, 'home.html', {})

def register(request):
    """register a user"""
    if request.method != 'POST':
        #empty form
        form = UserCreationForm
    else:
        #process form data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #log in, go to home
            password = request.POST['password1']
            auth_user = authenticate(
                username=new_user.username,
                password=password
            )
            login(request, auth_user)
            return redirect('home')
    return render(request, "registration/register.html", {"form": form})

@login_required
def success(request):
    if request.user.is_authenticated():
        us = request.user.username
    return HttpResponse(us + "logged in")
