from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from ideas.models import PostForm
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
def create_post(request):
    if request.method != 'POST':
        form = PostForm
        return render(request, 'new_post.html', {"form": form})
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect('home')


@login_required
def manage_profile(request):
    usr = request.user
    pfl = usr.profile
    if request.method == 'POST':
        if 'new_email' in request.POST:
            new_email = str(request.POST['new_email'])
            pfl.email = new_email
            pfl.save()
        if 'new_bio' in request.POST:
            new_bio = str(request.POST['new_bio'])
            pfl.bio = new_bio
            pfl.save()
    usr = request.user
    return render(request, 'account.html', {"user": usr})
