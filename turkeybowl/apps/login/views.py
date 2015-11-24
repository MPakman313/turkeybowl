from django.http import HttpResponse, Http404
from django.shortcuts import render
from apps.login.models import Player, Team

def index(request):
    context = {
        'teams': [
           { 'id': 1, 'content': 'Team1'},
           { 'id': 2, 'content': 'Team2'},
           { 'id': 3, 'content': 'Team3'},
           { 'id': 4, 'content': 'Team4'},
        ]
    }
    return render(request, 'login/index.html', context)

def dashboard(request, question_id):
    # teams = Team.objects.all():
    # players = Player.objects.all():
    context = {
        "id": team_id,
        "team": "Team5",
    }
    return render(request, 'login/dashboard.html', context)