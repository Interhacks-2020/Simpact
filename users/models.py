from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
import datetime

class User(AbstractUser):
    username = None
    is_volunteer = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email



class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?


'''
class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #Add what they can access here?
'''

'''
# this is temporary from the tutorial 
class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)

#end of temp


class perksForm(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'perksSubmit')
    perkName = forms.CharField(max_length = 100)
    perkPrice = forms.IntegerField(min_value = 1, max_value = 9999)
    productDurationFrom = forms.DateField(initial = datetime.date.today)
    productDurationTo = forms.DateField(initial = datetime.date.today)
    combinePerk = forms.BooleanField(required = False)
    uploadPerkPhoto = forms.ImageField() # (upload_to='images/')
    class Meta:
        db_table: "newperkstable"

    
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
   
'''

