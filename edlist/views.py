from django.shortcuts import render, HttpResponse

from .models import Item

def Edmarie(request):

# Create your views here.
	if request.method == 'POST':
		
		today = request.POST['today']
		org = request.POST['org']
		username = request.POST['username']
		batch = request.POST['batch']
		cern = request.POST['cern']
		gender = request.POST['gender']

		
		ems = Item()
		ems.today = today
		ems.org = org
		ems.username = username
		ems.batch = batch
		ems.cern = cern
		ems.gender = gender
		ems.save()
	
	return render(request,'Edmarie.html')


def Page(request):
	ems = Item.objects.all().order_by('today')
	return render(request,'okay.html', {'ems': ems})

