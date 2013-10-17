from django.db import models
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget

DEBATE_DAY_CHOICES = ('1st', '2nd')
PERIOD_CHOICES = ('1', '2', '3', '4', '5', '6', '7')
LOCATION_CHOICES = ('Library', 'Little_Theatre', 'Other_Location')

# Create your models here.

class debate(models.MODEL):
	topic = models.CharField(max_length=255)
	affirmative_team_name = models.CharField(unique = True, max_length=255)
	negative_team_name = models.CharField(unique = True, max_length=255)
	period = models.CharField(max_length=2, choices=PERIOD_CHOICES)
	date = models.DateField(widget=SelectDateWidget(days=DEBATE_DAY_CHOICES))
	location = models.CharField(max_length=255, choices=LOCATION_CHOICES)

	class Ordering:
				ordering = ['-date']

	def __unicode__(self):
				return u'%s' % self.topic

	def get_absolute_url(self):
				return reverse('debates.views.debates',args=[self.date])