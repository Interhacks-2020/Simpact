from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='simpact-home'),
    path('businessLogin', views.businessLogin, name='business-login'),
    path('npoLogin', views.npoLogin, name='npo-login'),
    path('volLogin', views.volLogin, name='vol-login'),
    path('about', views.simpactAbout, name='simpact-about'),
    
    path('opps/', views.all_events, name='show-events'),
    path('volListing/', views.all_volopps, name='vol-listing'),
    
    path('add_volopp/', views.add_volopp, name='add-volopp'),
    
    
    #path('', views.InsertPerks)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
