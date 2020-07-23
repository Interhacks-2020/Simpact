from django.db import models
from multiselectfield import MultiSelectField
from django_fields import DefaultStaticImageField

# Create your models here.

# Volunteer Opportunities
class VolOpp(models.Model):
    orgname = models.CharField('Organization Name', max_length=120, blank=True)
    vol_title = models.CharField('Title', max_length=200, blank=False)
    vol_description = models.TextField('Description', blank=False)
    vol_location = models.CharField('Location', max_length=200, blank=False)
    vol_date = models.DateTimeField('Date', blank=False)
    org_phone = models.CharField('Contact Phone', max_length=20, blank=True)
    age_requirements = models.IntegerField('Age Requirements', blank=False)
    points = models.IntegerField('Points Worth', blank=False)
    vol_photo = DefaultStaticImageField('Upload Image',upload_to='voloppimgs/', blank=True, default_image_path='/voloppimgs/default.png')
    
    FILTERS = (
            ('animal', 'Animals'),
            ('artmusic','Arts & Music'),
            ('edu', 'Education'),
            ('env', 'Environment'),
            ('health', 'Health & Medicine'),
            ('justice', 'Jusitce & Legal'),
            ('others', 'Others')
            )
    vol_filters = MultiSelectField(choices = FILTERS, default="")
    
    
    def __str__(self):
        return self.name
