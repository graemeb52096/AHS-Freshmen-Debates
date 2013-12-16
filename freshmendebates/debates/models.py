from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.utils.timezone import utc
import pytz
from django.utils import timezone
import logging

logger = logging.getLogger('logview.debugger')
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
	#R = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

class Negative(models.Model):
	Speaker1 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Speaker2 = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	CrossExamination = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	Argument = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	SlideShowScore = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)
	#R = models.CharField(max_length=2, choices=SCORE_CHOICES, default=5)

class SubmittedAffirmativeScore(models.Model):
	Speaker1 = models.CharField(max_length=3)
	Speaker2 = models.CharField(max_length=3)
	CrossExamination = models.CharField(max_length=3)
	Argument = models.CharField(max_length=3)
	SlideShowScore = models.CharField(max_length=3)
	#R = models.CharField(max_length=3)
	TeamNumber = models.CharField(max_length=20)
	def __unicode__(self):
				return u'%s' % self.TeamNumber

class SubmittedNegativeScore(models.Model):
	Speaker1 = models.CharField(max_length=3)
	Speaker2 = models.CharField(max_length=3)
	CrossExamination = models.CharField(max_length=3)
	Argument = models.CharField(max_length=3)
	SlideShowScore = models.CharField(max_length=3)
	#R = models.CharField(max_length=3)
	TeamNumber = models.CharField(max_length=20)
	def __unicode__(self):
				return u'%s' % self.TeamNumber

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

class CustomUser(models.Manager):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(('email address'), max_length=254, unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])