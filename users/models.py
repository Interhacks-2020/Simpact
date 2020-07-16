from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_volunteer = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?
# Create your models here.

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?
# Create your models here.

class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?
# Create your models here.


class perksForm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'perksSubmit')
    perkName = forms.CharField(max_length = 100)
    perkPrice = forms.IntegerField(min_value = 1, max_value = 9999)
    productDurationFrom = forms.DateField(initial = datetime.date.today)
    productDurationTo = forms.DateField(initial = datetime.date.today)
    combinePerk = forms.BooleanField(required = False)
    uploadPerkPhoto = forms.ImageField(upload_to='images/')
    
    
class advertisementForm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'perksSubmit')
    advTitle = forms.CharField(max_length = 100)
    advDescription = forms.Textarea(max_length = 9999)
    uploadAdvPhoto = forms.ImageField(upload_to='advimages/')
    customAdHomepage = forms.BooleanField(required = False)
    customAdSearch = forms.BooleanField(required = False)
    customAdBanner = forms.BooleanField(required = False)
    advDurationFrom = forms.DateField(initial = datetime.date.today)
    advDurationTo = forms.DateField(initial = datetime.date.today)
   

