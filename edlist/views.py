from django.shortcuts import redirect, render
#from django.http import HttpResponse
from .models import Mainpage, Officer, Member, Contribute, Contribution2, Activities, ActivitiesDisplay, survey
# from .models import User, Info


def Main1(request):

	if request.method == 'POST':

		organization = MainPage.objects.create()
		Mainpage.objects.create(
			organization = request.POST['organization'],
			position = request.POST['position'],
			)

		return redirect('Contibute')
		
		em = Mainpage()
		organization = request.POST['organization'],
		position = request.POST['position']
		em.save()

	return render(request,'Main1.html')

def Page(request):
	
	em = Mainpage.objects.all().order_by('organization')
	return render(request,'Contibute.html', {'em': em})


'''


# Create your views here.
def Edmarie(request):

	if request.method == 'POST':

		university = User.objects.create()
		Item.objects.create(
			today = request.POST['today'],
			org = request.POST['org'], 
			username = request.POST['username'],
			batch = request.POST['batchs'], 
			cern = request.POST['cern'],
			gender = request.POST['gender'],
			)
		return redirect('okay/')


		# today = request.POST['today']
		# org = request.POST['org']
		# username = request.POST['username']
		# batchs = request.POST['batchs']
		# cern = request.POST['cern']
		# gender = request.POST['gender']

		
		ems = Item()
		ems.today = today
		ems.org = org
		ems.username = username
		ems.batchs = batchs
		ems.cern = cern
		ems.gender = gender
		ems.save()
	
	return render(request,'Edmarie.html')


def Page(request):
	ems = Item.objects.all().order_by('today')
	return render(request,'okay.html', {'ems': ems})


def Edmarie(request):

	return render(request,'trylang.html')

def Officer(request):

	officerId=officer.objects.create(
		firstname = request.POST['name'],
		middle = request.POST['middle'],
		surname = request.POST['sur'],
		course = request.POST['course'],
		section = request.POST['year'],
		number = request.POST['number'],
		email = request.POST['email'],
		position = request.POST['posi'],
		gender = request.POST['gender'],
		today = request.POST['birthday'],
		)

	return render(request,'trylang2/')


def SecondPage(request):

	customerId=Customer.objects.create(
		firstname = request.POST['name'],
		middle = request.POST['contact'],
		surname = request.POST['reserve'],
		course = request.POST['name'],
		section = request.POST['contact'],
		number = request.POST['reserve'],
		email = request.POST['name'],
		gender = request.POST['reserve'],
		today = request.POST['reserve'],
		)

	return render(request,'nextpage.html')


def ThirdPage(request):

	# customerId=Customer.objects.get(id=customerId)

	resortId=Resort.objects.create(
		resort = request.POST['resort'])

	admitId=Admission.objects.create(
		entrance = request.POST['entrance'],
		admit = request.POST['admit'],
		)

	cottageId=Cottage.objects.create(
		cottage = request.POST['cottage'])

	return render(request,'receipt.html')


def FourthPage(request):

	# customerId=Customer.objects.get(id=customerId)

	resortId=Resort.objects.create(
		resort = request.POST['resort'])

	admitId=Admission.objects.create(
		entrance = request.POST['entrance'],
		admit = request.POST['admit'],
		)

	cottageId=Cottage.objects.create(
		cottage = request.POST['cottage'])

	return render(request,'receipt.html')


def FifthPage(request):

	# customerId=Customer.objects.get(id=customerId)

	resortId=Resort.objects.create(
		resort = request.POST['resort'])

	admitId=Admission.objects.create(
		entrance = request.POST['entrance'],
		admit = request.POST['admit'],
		)

	cottageId=Cottage.objects.create(
		cottage = request.POST['cottage'])

	return render(request,'receipt.html')'''



