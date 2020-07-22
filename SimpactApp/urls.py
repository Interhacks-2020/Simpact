from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='simpact-home'),
    path('businessLogin', views.businessLogin, name='business-login'),
    path('npoLogin', views.npoLogin, name='npo-login'),
    path('volLogin', views.volLogin, name='vol-login'),
    path('about', views.simpactAbout, name='simpact-about'),
    path('volunteerDescription' , views.volunteerDescription, name='volunteer-description'),
    path('volunteerDashboard' , views.volunteerDashboard, name='volunteer-dashboard'),
    
    
    path('opps/', views.all_events, name='show-events')
    
    #path('', views.InsertPerks)
]
