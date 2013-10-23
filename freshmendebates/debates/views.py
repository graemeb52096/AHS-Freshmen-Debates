from django.shortcuts import render, get_object_or_404
from debates.models import debatetopic
from debates.models import debatelocations
from debates.models import debatedates

# Create your views here.

def judge(request):
	#get the debates that are on
	debate = debatetopic.objects.filter()
	#Now return the rendered template
	return render(request,'debates/judge.html',{'debatetopic': debatetopic})
def debates(request):
	#get the debates that are on
	debate = debatetopic.objects.filter(debatetopic, topic=topic)
	#Now return the rendered template
	return render(request,'debates/judge.html',{'debatetopic': debatetopic})