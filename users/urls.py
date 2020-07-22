from django.contrib import admin
from django.urls import path

from .views import businesses, ngo, volunteer
from SimpactApp import views as simpactviews


urlpatterns = [
    path('',simpactviews.home,name="home"),
    path('accounts/business/',businesses.sign_up,name="sign-up")
]