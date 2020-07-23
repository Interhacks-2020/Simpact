from django.db import models

# Create your models here.

# Volunteer Opportunities
class VolOpp(models.Model):
    orgname = models.CharField('Organization Name', max_length=120)
    orgdescription = models.TextField(blank=True)
    age_requirements = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)
    vol_date = models.DateTimeField('Event Date')
    

    def __str__(self):
        return self.name
