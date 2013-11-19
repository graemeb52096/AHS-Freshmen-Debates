from django.shortcuts import render, get_object_or_404
from debates.models import Topic,Location,Date,Teacher
from debates.forms import AffirmativeScore,NegativeScore
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import logging



# Create your views here.


#get the debate that are on
def judge(request):
	logger = logging.getLogger('logview.debugger')
	
	Submit_form = 'null'
	Affform = AffirmativeScore()
	Negform = NegativeScore()
	if request.method == 'GET':
		Affform = AffirmativeScore()
		Negform = NegativeScore()
		logger.debug('Getting request method GET!')
	elif request.method == 'POST':
		logger.debug('Getting request method Post!')
		logger.debug(request.POST)
	 	if 'form_Positive' in request.POST:
	 		logger.debug('Form is Positive')
			Affform = AffirmativeScore(request.POST)
			Submit_form = 'aff'
	 		if Affform.is_valid():
				Speaker1 = Affform.cleaned_data.get('Speaker1')
				Speaker2 = Affform.cleaned_data.get('Speaker2')
				CrossExamination = Affform.cleaned_data.get('CrossExamination')
				SlideShowScore = Affform.cleaned_data.get('SlideShowScore')
				Argument = Affform.cleaned_data.get('Argument')
				logger.debug('Affirmative form is valid!')
		elif 'form_Negative' in request.POST:
			logger.debug('Form is Negative')
			Negform = NegativeScore(request.POST)
			Submit_form = 'neg'
			if Negform.is_valid():
				Speaker1 = Negform.cleaned_data.get('Speaker1')
				Speaker2 = Negform.cleaned_data.get('Speaker2')
				CrossExamination = Negform.cleaned_data.get('CrossExamination')
				SlideShowScore = Negform.cleaned_data.get('SlideShowScore')
				Argument = Negform.cleaned_data.get('Argument')
				#msg = "The operation has been received correctly."
				#print request.POST
				#return render_to_response('debates/scoring_upload.html', {'msg':msg}, context_instance=RequestContext(request))
				logger.debug('Negative form is valid!')
				#return render_to_response(msg)
		if request.is_ajax():
			logger.debug('Request is ajax')
			return render(request, 'debates/scoring_upload.html')
			msg = "The operation has been received correctly."
			print request.POST
#Now return the rendered template
			return render_to_response('debates/scoring_upload.html', {'msg':msg}, context_instance=RequestContext(request))

	return render(request,'debates/judge.html', {
		'Affirmative_Form':Affform, 'Negative_Form':Negform,
	})

def handle(request):

	return render(request,'debates/scoring_upload.html', {
	})

def splash(request):

	return render(request,'debates/Splash.html', {
	})

def teacher(request):

	return render(request,'debates/Teacher.html', {
	})

def teacherselector(request):

	return render(request,'debates/TeacherSelector.html', {
	}) 

def teamcreate(request):

	return render(request,'debates/TeamCreate.html', {
	})	

def debateselector(request):

	return render(request,'debates/DebateSelector.html', {
	})
