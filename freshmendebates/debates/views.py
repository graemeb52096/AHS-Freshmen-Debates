from django.shortcuts import render, get_object_or_404
from debates.models import Topic,Location,Date,Teacher
from debates.forms import AffirmativeScore,NegativeScore
from django.http import HttpResponseRedirect

# Create your views here.

def Aff(request):
	#get the debate that are on

	if request.method == 'GET':
        	Affform = AffirmativeScore()
	else:
		# A POST request: Handle Form Upload
        	Affform = AffirmativeScore(request.POST) # Bind data from request.POST into a PostForm
		 # If data is valid, proceeds to create a new post and redirect the user
        	if Affform.is_valid():
           		SlideShowScore = Affform.cleaned_data['SlideShowScore']
            	Speaker1 = Affform.cleaned_data['Speaker1']
            	Speaker2 = Affform.cleaned_data['Speaker2']
            	CrossExamination = Affform.cleaned_data['CrossExamination']
            	Argument = Affform.cleaned_data['Argument']
            	post = m.Post.objects.create(
            		SlideShowScore=SlideShowScore, Speaker1=Speaker1, Speaker2=Speaker2, CrossExamination=CrossExamination, Argument=Argument
            	)
            	return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))


	#return render_to_response('judge.html',{'form':form}, context_instance=RequestContext(context))
	#Now return the rendered template
	return render(request,'debates/judge.html', {
		'form': Affform,
		})

def Neg(request):
	#get the debate that are on

	if request.method == 'GET':
        	Negform = AffirmativeScore()
	else:
		# A POST request: Handle Form Upload
        	Negform = AffirmativeScore(request.POST) # Bind data from request.POST into a PostForm
		 # If data is valid, proceeds to create a new post and redirect the user
        	if Negform.is_valid():
           		SlideShowScore = Negform.cleaned_data['SlideShowScore']
            	Speaker1 = Negform.cleaned_data['Speaker1']
            	Speaker2 = Negform.cleaned_data['Speaker2']
            	CrossExamination = Negform.cleaned_data['CrossExamination']
            	Argument = Negform.cleaned_data['Argument']
            	post = m.Post.objects.create(
            		SlideShowScore=SlideShowScore, Speaker1=Speaker1, Speaker2=Speaker2, CrossExamination=CrossExamination, Argument=Argument
            	)
            	return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))


	#return render_to_response('judge.html',{'form':form}, context_instance=RequestContext(context))
	#Now return the rendered template
	return render(request,'debates/judge.html', {
		'form': Negform,
		})
