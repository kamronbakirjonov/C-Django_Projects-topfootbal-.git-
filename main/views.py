from django.shortcuts import render
from django.views import View

from main.models import Club


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()

        context = {
            'clubs': clubs,
        }
        return render(request, 'clubs.html',context )




class LatesttransfersView(View):
    def get(self, request, ):
        transfers = LatesttransfersView.objects.order_by('-created_at')
        context = {
            'transfers': transfers,
        }
        return render(request, 'latesttansfers.html', context )
class PLayersView(View):
    def get(self, request):
        players = PLayersView.objects.order_by('-price')
        context = {
             'players': players,
        }
        return render(request, 'players.html',context )

class U_20playersView(View):
    def get(self, request):
        players = PLayersView.objects.filter(age__lte=20).order_by('-price')
        context = {
            'players': players,
        }
        return render(request, 'U_20players.html',context )

class tryoutsView(View):
    def get(self, request):
        return render(request, 'tryouts.html' )
class statsView(View):
    def get(self, request):
        return render(request, 'stats.html' )
class aboutView(View):
    def get(self, request):
        return render(request, 'about.html' )
