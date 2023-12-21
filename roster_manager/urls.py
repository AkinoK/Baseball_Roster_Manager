from django.urls import path
from . import views
from .views import DeletePlayerView


urlpatterns = [
    path('roster_list/', views.roster_list, name='roster_list'),
    path('add_player/', views.add_player, name='add_player'),
    path('edit_player/<int:player_id>/', views.edit_player, name='edit_player'),
    # path('delete_player/<int:player_id>/', views.delete_player, name='delete_player'),
    # path('delete-player/<int:player_id>/', DeletePlayerView.as_view(), name='delete_player'),
    path('delete_player/<int:player_id>/', DeletePlayerView.as_view(), name='delete_player'),

]
