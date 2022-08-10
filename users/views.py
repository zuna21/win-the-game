from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from games.models import Game
from .forms import CustomUserCreationForm

# Create your views here.
def loginUser(request):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try: 
            user  = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username OR password is incorrect')
    
    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,
    }
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')


    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account created!')

            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error has occurred during registration')
    
    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,

        'form': form,
    }
    return render(request, 'users/register.html', context)