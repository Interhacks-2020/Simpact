from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'SimpactApp/index.html')

def businessLogin(request):
    return render(request, 'SimpactApp/businesslogin.html')

def npoLogin(request):
    return render(request, 'SimpactApp/npologin.html')

def volLogin(request):
    return render(request, 'SimpactApp/volunteerlogin.html')

def npoDash(request):
    return render(request, 'Users/dashboardbase.html')

def simpactAbout(request):
    return HttpResponse('<h1> this is the about page <h1>')


def testPath(request):
    return HttpResponse('<h1> hello testing <h1>')





# Create your views here.
