from django import forms
from django.forms import ModelForm
from .models import VolOpp

class VolOppForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = VolOpp
        fields = '__all__'
