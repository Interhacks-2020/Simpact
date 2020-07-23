from django.contrib import admin
from django.urls import path

from .views import businesses, ngo, volunteer
from SimpactApp import views as simpactviews


urlpatterns = [
    path('',simpactviews.home,name="home"),
    path('accounts/business/',businesses.sign_up,name="sign-up"),
    path("logout", businesses.logout_request, name="logout"),
    path("bdash", businesses.business_dashboard, name="bdash"),
]