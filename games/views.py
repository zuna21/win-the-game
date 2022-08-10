from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Game, Comment
from .forms import CommentForm, ReplyForm

# Create your views here.
def home(request):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    # ostatak
    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,
    }
    return render(request, 'games/home.html', context)

def game(request, pk):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    # ostatak
    game = Game.objects.get(id=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user.profile
            comment.game = game
            comment.save()
            messages.success(request, 'Your comment was successfully submitted!')

            return redirect('game', pk=game.id)

    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,

        'game': game,
        'form': form,
    }
    return render(request, 'games/game.html', context)


def history(request):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    # ostatak
    games = Game.objects.filter(is_history=True)

    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,
        
        'games': games,
    }

    return render(request, 'games/history.html', context)

@login_required(login_url='login')
def reply(request, pk):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    # ostatak
    comment = Comment.objects.get(id=pk)
    form = ReplyForm()

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.owner = request.user.profile
            reply.comment = comment
            reply.save()
            messages.success(request, 'Your reply was successfully submitted!')

            return redirect('game', pk=comment.game.id)

    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,

        'comment': comment,
        'form': form,
    }

    return render(request, 'games/reply.html', context)


@login_required(login_url='login')
def premium(request):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    # ostatak
    games = Game.objects.filter(category='PRE').order_by('-created')[:5]
    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,

        'games': games,
    }

    return render(request, 'games/premium.html', context)


def contact(request):
    # za navbar
    game_low = Game.objects.filter(category='LOW').latest('created')
    game_medium = Game.objects.filter(category='MED').latest('created')
    game_high = Game.objects.filter(category='HIG').latest('created')

    context = {
        'game_low': game_low,
        'game_medium': game_medium,
        'game_high': game_high,

    }

    return render(request, 'games/contact.html', context)