from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='simpact-home'),
    path('businessLogin', views.businessLogin, name='business-login'),
    path('npoLogin', views.npoLogin, name='npo-login'),
    path('volLogin', views.volLogin, name='vol-login'),
    path('npodash', views.npoDash, name='npo-dash'),
    path('about', views.simpactAbout, name='simpact-about'),
    path('opps/', views.all_events, name='show-events'),

    #path('', views.InsertPerks)
]
