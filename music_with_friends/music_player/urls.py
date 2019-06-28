from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='music_player-home'),
    path('home/', views.home, name='music_player-home'),
    path('login/', views.login, name='music_player-login'),
    path('dashboard/', views.dashboard, name='music_player-dashboard')
]