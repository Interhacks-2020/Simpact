from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='simpact-home'),
    path('businessLogin', views.businessLogin, name='business-login'),
    path('npoLogin', views.npoLogin, name='npo-login'),
    path('volLogin', views.volLogin, name='vol-login'),
    path('npodash', views.npoDash, name='npo-dash'),
    path('about', views.simpactAbout, name='simpact-about'),

    path('volListing/', views.all_volopps, name='vol-listing'),
    path('volListing/voloppdescription', views.voloppdescription, name='volopp-description'),
    path('volDashboard', views.volDashboard, name='vol-dash'),
    
    path('npoDashboard', views.npoDashboard, name='npo-dash'),
    path('add_volopp/', views.add_volopp, name='add-volopp'),
    
    path('busPerks', views.busPerks, name='bus-perks'),
    path('busNewPerks', views.busNewPerks, name='bus-newperks'),
    path('busPromote', views.busPromote, name='bus-promote'),
    
    #path('', views.InsertPerks),
    path('opps/', views.all_events, name='show-events'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
