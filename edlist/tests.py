from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from edlist.views import Edmarie
from django.urls import resolve
#For Models testing
from edlist.models import Item, User
from django.urls import reverse

class mainTest(TestCase):

	def mainpage_html(self):
		found = resolve('/')
		self.assertEqual(found.func, Edmarie)
		
	def test(self):
		request = HttpRequest()
		response = Edmarie(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Edmarie.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'Edmarie.html')	
		self.assertIn('<title>TUP-C ACSO</title>', html)
		self.assertIn('<h1 style="color:white; font-size: 45px; background-color:maroon">TUP-Cavite Student Organization</h1>', html)
		self.assertIn('<center>', html)
		self.assertIn('</center>', html)
		self.assertIn('<p><b> Date: </b></p>', html)
		self.assertIn('<label id="orgs"><b>Accredited Student Organization:</b></label>', html)
		self.assertIn('<input bold type="text" id="org" name="org" placeholder="e.g. University Student Organization">', html)
		self.assertIn('<label id="usernames"><b>Full Name:</b></label>', html)
		self.assertIn('<input bold type="text" id="username" name="username" placeholder="e.g. Lyra F. Eria">', html)
		self.assertIn('<label id="concerns"><b>Student Number:</b></label>', html)
		self.assertIn('<br>', html)
		self.assertIn('<input bold type="text" id="cern" name="cern" placeholder="e.g. TUPC-20-00-00">', html)
		self.assertIn('<p id="p2"><b>Gender:</b></p>', html)
		self.assertIn('<input type="radio"   id="male" name="gender" value="Male">', html)
		self.assertIn('<label id="circle">Male</label>', html)
		self.assertIn('<input type="radio"   id="female" name="gender" value="Female">', html)
		self.assertIn('<label id="circle">Female</label>', html)
		self.assertIn('<input type="submit" name="submit1" id="submit2" value="Submit">', html)

		self.assertTrue(html.strip().endswith('</html>'))

class ORM(TestCase):
	def test_orm(self):
		Item1 = Item()
		Item1.today = '2004-04-04'
		Item1.save()
		Item2 = Item()
		Item2.org = 'Future Educators Organization'
		Item2.save()
		Item3 = Item()
		Item3.username = 'Edmarie L. Suatin'
		Item3.save()
		Item4 = Item()
		Item4.batchs = 'BSCE-1A'
		Item4.save()
		Item5 = Item()
		Item5.cern = 'TUPC-18-04-05'
		Item5.save()
		Item6 = Item()
		Item6.gender = 'Female'
		Item6.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		self.assertEqual(Item1.today, '2004-04-04')
		self.assertEqual(Item2.org, 'Future Educators Organization')
		self.assertEqual(Item3.username, 'Edmarie L. Suatin')
		self.assertEqual(Item4.batchs, 'BSCE-1A')
		self.assertEqual(Item5.cern, 'TUPC-18-04-05')
		self.assertEqual(Item6.gender, 'Female')

class Views(TestCase):
	def test_views(self):
		Item.objects.create(today='2004-04-04', 
			org='org', username='username',
			batch='batchs', cern='cern', gender='female')
		response = self.client.get('/app/views.Edmarie/')

class ORM(TestCase):
	def test_test(self):

		Item1 = Item()
		Item1.today = '2019-02-05'
		Item1.save()
		Item2 = Item()
		Item2.org = 'Engineering Honor Society'
		Item2.save()
		Item3 = Item()
		Item3.username = 'Diane Faye S. Tipanao'
		Item3.save()
		Item4 = Item()
		Item4.batchs = 'BET-MT-3A'
		Item4.save()
		Item5 = Item()
		Item5.cern = 'TUPC-20-02-04'
		Item5.save()
		Item6 = Item()
		Item6.gender = 'Male'
		Item6.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 6)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		save6 = saveall[5]
		self.assertEqual(Item1.today, '2019-02-05')
		self.assertEqual(Item2.org, 'Engineering Honor Society')
		self.assertEqual(Item3.username, 'Diane Faye S. Tipanao')
		self.assertEqual(Item4.batchs, 'BET-MT-3A')
		self.assertEqual(Item5.cern, 'TUPC-20-02-04')
		self.assertEqual(Item6.gender, 'Male')


class ListViewTest(TestCase):

	def test_uses_list_template(self):
		university = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Edmarie.html')
	def test_uses_home_template(self):
		response = self.client.get('/okay/')
		self.assertTemplateUsed(response, 'okay.html')
	def test_displays_all_list_items(self):
		university = User.objects.create()
		today = Item.objects.create(today='2004-04-04')
		org = Item.objects.create(org='org')
		username = Item.objects.create(username='username')
		batch = Item.objects.create(batch='batchs')
		cern = Item.objects.create(cern='cern')
		gender = Item.objects.create(gender='gender')
		response = self.client.get('/')
		self.assertIn('today', response.content.decode())
		self.assertIn('org', response.content.decode())
		self.assertIn('username', response.content.decode())
		self.assertIn('batch', response.content.decode())
		self.assertIn('cern', response.content.decode())
		self.assertIn('gender', response.content.decode())
		today = Item.objects.get(today="2004-04-04")
		org = Item.objects.get(org="org")
		username = Item.objects.get(username="username")
		batchs = Item.objects.get(batch="batchs")
		cern = Item.objects.get(cern="cern")
		gender = Item.objects.get(gender="gender")
		self.assertEqual(Item.objects.count(), 6)
		
class Views(TestCase):
	def setUp(self):
		today = Item.objects.create()
		org = Item.objects.create()
		username = Item.objects.create()
		batch = Item.objects.create()
		cern = Item.objects.create()
		gender = Item.objects.create()
		
		Item.objects.create(
			today = '2004-04-04',
			org = 'Future Educators Organization',
			username = 'Edmarie L. Suatin',
			batch = 'BSCE-1A',
			cern = 'TUPC-18-04-05',
			gender = 'Female',
			)
		self.client.post('/okay/', today='2004-04-04')
		
		#response 
		self.client.post('/okay/')

		self.assertEqual(Item.objects.count(), 7)

	def test_redirect_view(self):
		today = Item.objects.get(today="2004-04-04")
		org = Item.objects.get(org="Future Educators Organization")
		username = Item.objects.get(username="Edmarie L. Suatin")
		batchs = Item.objects.get(batch="BSCE-1A")
		cern = Item.objects.get(cern="TUPC-18-04-05")
		gender = Item.objects.get(gender="Female")

		response = self.client.post('/okay/')

class URL(TestCase):

	def urls(self):
		found = resolve()
		self.assertEqual(found.func, homepage)
		self.assertEqual(found.func, ed)

		url = reverse('Edmarie')
		self.assertEqual(resolve(url).func, homepage)

		url = reverse('okay')
		self.assertEqual(resolve(url).func, ed)


class Models(TestCase):

	def models(self, 
		today="test1", 
		org="test2", 
		username="test3", 
		batch="test4", 
		cern="test5", 
		gender="test6" ):
		
		return User.objects.create()
		return Item.objects.create(
			today="today", 
			org="org", 
			username="username", 
			batch="batchs", 
			cern="cern", 
			gender="gender")

	def test_whatever_creation(self):
		em = self.models()
		self.assertTrue(isinstance(em, User))
		self.assertFalse(isinstance(em, Item))




		