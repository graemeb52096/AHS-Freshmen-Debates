from django.shortcuts import render, get_object_or_404
from blog.models import debate

# Create your views here.

def judge(request):
	#get the debates that are on
	debate = debate.objects.filter(date=Today)
	#Now return the rendered template
	return render(request,'debates/judge.html',{'debate': debate})

def summary(request, date, period, location):
	#Get summary of debate times and locations
	debate = get_object_or_404(debate, date=date, period=period, location=location)
	#Now return the rendered template
	return render(request, 'debates/summary.html', {'debate':debate})