from django.db import models
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget

DEBATE_DAY_CHOICES = ('1st', '2nd')
PERIOD_CHOICES = ('1', '2', '3', '4', '5', '6', '7')
LOCATION_CHOICES = ('Library', 'Little_Theatre', 'Other_Location')

SCORE_CHOICES = (
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

# Create your models here.
class Affirmative(models.Model):	
	Speaker1 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Speaker2 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	CrossExamination = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Argument = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	SlideShowScore = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

class Negative(models.Model):
	Speaker1 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Speaker2 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	CrossExamination = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Argument = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	SlideShowScore = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

# class Team():

class Topic(models.Model):
	topic = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.topic


class Location(models.Model):
	location = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.location

	
class Date(models.Model):
	date = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.date

class Teacher(models.Model):
	teahcer = models.CharField(max_length=255)
	def __unicode__(self):
				return u'%s' % self.teahcer

class SCORE_OPTIONS(models.Model):
	SCORE_CHOICES = [(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10')]
	scores = models.BigIntegerField(verbose_name='scores:', choices=SCORE_CHOICES)