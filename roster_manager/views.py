# Author: Akino Kashima
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.http import JsonResponse
from .models import Player
from .forms import PlayerForm

# def roster_list(request):
#     players = Player.objects.all()
#     return render(request, 'roster_manager/roster_list.html', {'players': players})

def roster_list(request):
    players = Player.objects.all()
    context = {'players': players}  # Include any other context data as needed
    return render(request, 'roster_manager/roster_list.html', context)


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('roster_list') 
    else:
        form = PlayerForm()

    return render(request, 'roster_manager/add_edit_player.html', {'form': form})

def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
        return redirect('roster_list') 
    else:
        form = PlayerForm(instance=player)
    
    return render(request, 'roster_manager/add_edit_player.html', {'form': form, 'player': player})

# class DeletePlayerView(View):
#     def post(self, request, player_id):
#         player = get_object_or_404(Player, id=player_id)
#         player.delete()
#         return redirect(reverse('roster_list'))
    
class DeletePlayerView(View):
    def post(self, request, player_id):
        try:
            player = get_object_or_404(Player, id=player_id)
            player.delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})