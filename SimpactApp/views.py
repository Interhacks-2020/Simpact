from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Simpact HTML Files/index.html')

def simpactAbout(request):
    return HttpResponse('<h1> this is the about page <h1>')





# Create your views here.
