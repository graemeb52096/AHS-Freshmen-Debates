from django.db import models
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget

DEBATE_DAY_CHOICES = ('1st', '2nd')
PERIOD_CHOICES = ('1', '2', '3', '4', '5', '6', '7')
LOCATION_CHOICES = ('Library', 'Little_Theatre', 'Other_Location')

# Create your models here.

class Topic(models.Model):
	topic = models.CharField(max_length=255)


class Location(models.Model):
	location = models.CharField(max_length=255)

	
class Date(models.Model):
	dates = models.CharField(max_length=255)

class Teacher(models.Model):
	dates = models.CharField(max_length=255)
