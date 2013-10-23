from django.db import models
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget

DEBATE_DAY_CHOICES = ('1st', '2nd')
PERIOD_CHOICES = ('1', '2', '3', '4', '5', '6', '7')
LOCATION_CHOICES = ('Library', 'Little_Theatre', 'Other_Location')

# Create your models here.

class Topics(models.Model):
	topic = models.CharField(max_length=255)


	class Meta:
				ordering = ['-topic']

	def __unicode__(self):
				return u'%s' % self.topic

	def get_absolute_url(self):
				return reverse('debates.views.debates',args=[self.date])

class debatelocations(models.Model):
	location = models.CharField(max_length=255)

	class Meta:
				ordering = ['-location']

	def __unicode__(self):
				return u'%s' % self.location

	def get_absolute_url(self):
				return reverse('debates.views.debates',args=[self.date])

class debatedates(models.Model):
	dates = models.CharField(max_length=255)

	class Meta:
				ordering = ['-location']

	def __unicode__(self):
				return u'%s' % self.location

	def get_absolute_url(self):
				return reverse('debates.views.debates',args=[self.date])