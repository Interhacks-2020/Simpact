
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction 
from django.forms.utils import ValidationError

from users.models import Business, Volunteer, User

'''
class VolunteerSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset = Subject.objects.all(),
        widget = forms.CheckboxSelectMultiple
        required = True
    )

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().sav(commit = False)
        user.is_volunteer = True
        user.save()
        volunteer = Volunteer.objects.create(user = user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user
'''
class BusinessSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_business = True
        user.save()
        business = Business.objects.create(user = user)
        return user


'''
class NgoSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset = Subject.objects.all(),
        widget = forms.CheckboxSelectMultiple
        required = True
    )

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().sav(commit = False)
        user.is_ngo = True
        user.save()
        ngo = Ngo.objects.create(user = user)
        ngo.interests.add(*self.cleaned_data.get('interests'))
        return user

        
class CompanyPerks(forms.Form):
    
    #this is where the user goes after the form has been submitted
    return HttpResposeRedirect('/perks/')
'''

