from django.urls import path

from .views import *

urlpatterns =[
    path('',IndexView.as_view(),name='index'),
    path ('clubs/',ClubsView.as_view(),name='clubs'),
    path('latesttransfers/', LatesttransfersView.as_view(), name='transfers'),
    path('players/',PLayersView.as_view(), name='players'),
    path('U_20players/',U_20playersView.as_view(), name='U_20'),
    path('tryouts/',tryoutsView.as_view(), name='tryouts'),
    path('stats/',statsView.as_view(), name='stats'),
    path('about/',aboutView.as_view(), name='about'),

]