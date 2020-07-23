import django_filters

from .models import *

class VolOppFilter(django_filters.FilterSet):
    class Meta:
        model = VolOpp
        fields = '__all__'
