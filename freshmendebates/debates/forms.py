from django import forms
from django.db import models
from django.forms import ModelForm
from debates.models import Affirmative,Negative

SCORE_CHOICES = (
		(5,'5'),
		(6,'6'),
		(7,'7'),
		(8,'8'),
		(9,'9'),
		(10,'10')
		)
scores = forms.ChoiceField(widget=forms.RadioSelect(), choices=SCORE_CHOICES)


class AffirmativeScore(ModelForm):
		SlideShowScore = scores.choices
		Speaker1 = scores.choices
		Speaker2 = scores.choices
		CrossExamination = scores.choices
		Argument = scores.choices
		class Meta:
			model = Affirmative

class NegativeScore(ModelForm):
		SlideShowScore = scores.choices
		Speaker1 = scores.choices
		Speaker2 = scores.choices
		CrossExamination = scores.choices
		Argument = scores.choices
		class Meta:
			model = Negative