from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<doctype>...')

def simpactAbout(request):
    return HttpResponse('<h1> this is the about page <h1>')

# Create your views here.
