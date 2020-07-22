from django.shortcuts import render
from django.http import HttpResponse

from .models import VolOpp

def home(request):
    return render(request, 'SimpactApp/index.html')

def businessLogin(request):
    return render(request, 'SimpactApp/businesslogin.html')

def npoLogin(request):
    return render(request, 'SimpactApp/npologin.html')

def volLogin(request):
    return render(request, 'SimpactApp/volunteerlogin.html')

def simpactAbout(request):
    return HttpResponse('<h1> this is the about page <h1>')

def volunteerDescription(request):
	return render( request, 'SimpactApp/volunteerdescription.html')



def volunteerDashboard(request):
	return render( request, 'SimpactApp/volunteerdashboard.html')






def testPath(request):
    return HttpResponse('<h1> hello testing <h1>')


#testing 
def all_events(request):
    event_list = VolOpp.objects.all()
    return render(request,
        'SimpactApp/volopp_list.html',
        {'event_list': event_list}
    )


# Create your views here.
