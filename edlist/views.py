from django.shortcuts import redirect, render
#from django.http import HttpResponse
from .models import Organization, OfficerDetails, MemberDetails, ReportDetails, ActivitiesDetails
# from .models import User, Info


def home(request):

	return render(request,'home.html')

def org(request):

		'''if request.method == 'POST':

		organization = MainPage.objects.create()
		Mainpage.objects.create(
			organization = request.POST['organization'],
			position = request.POST['position'],
			)

		return redirect('Contibute')
		
		em = Mainpage()
		organization = request.POST['organization'],
		position = request.POST['position']
		em.save()'''

		return render(request,'organization.html')

def member(request):

	'''if request.method == 'POST':

		organization = MainPage.objects.create()
		Mainpage.objects.create(
			organization = request.POST['organization'],
			position = request.POST['position'],
			)

		return redirect('Contibute')
		
		em = Mainpage()
		organization = request.POST['organization'],
		position = request.POST['position']
		em.save()'''
	return render(request,'dual.html')

# Create your views here.
def officer(request):

	return render(request,'activities.html')

def report(request):
	
	#em = Mainpage.objects.all().order_by('classification')
	return render(request,'reports.html')


# Create your views here.
def play(request):

	return render(request,'display.html')