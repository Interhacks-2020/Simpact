from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='simpact-home'),
    path('businessLogin', views.businessLogin, name='business-login'),
    path('npoLogin', views.npoLogin, name='npo-login'),
    path('about', views.simpactAbout, name='simpact-about'),
    
    #path('', views.InsertPerks)
]
