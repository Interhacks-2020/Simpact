from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction 

from users.models import Volunteer, Subject, User

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

        