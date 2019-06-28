from django.shortcuts import render


def home(request):
    return render(request, 'music_player/home.html')

def login(request):
    return render(request, 'music_player/login.html')

def dashboard(request):
    return render(request, 'music_player/dashboard.html')