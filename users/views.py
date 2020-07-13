from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from models import perksForm


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Create your views here.

# Insert new perks into datatable
def InsertPerks(request):
    if request.method == 'POST':
        if request.POST.get('perkName') and request.POST.get('perkPrice') and request.POST.get('productDurationFrom') and request.POST.get('productDurationTo') and request.POST.get('uploadPerkPhoto'):
            saverecord = perksForm()
            saverecord.perkName = request.POST.get('perkName')
            saverecord.perkPrice = request.POST.get('perkPrice')
            saverecord.productDurationFrom = request.POST.get('productDurationFrom')
            saverecord.productDurationTo = request.POST.get('productDurationTo')
            saverecord.uploadPerkPhoto = request.POST.get('uploadPerkPhoto')
            saverecord.save()
            
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'templates/users/newperks.html')
    else:
            return render(request, 'templates/users/newperks.html')
