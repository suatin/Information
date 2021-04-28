from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from edlist.views import Edmarie
from django.urls import resolve
#For Models testing
from edlist.models import Item

class IndexTest(TestCase):

	def html_index_root_mainpage_pwede_din_homepage_basta(self):
		found = resolve('/')
		self.assertEqual(found.func, Edmarie)

		
	def test_index_returns_correct_view(self):
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
		self.assertIn('<input bold type="text" id="cern" name="cern" placeholder="e.g. TUPC-20-**-**">', html)
		self.assertIn('<p id="p2"><b>Gender:</b></p>', html)
		self.assertIn('<input type="radio"   id="male" name="gender" value="Male">', html)
		self.assertIn('<label id="circle">Male</label>', html)
		self.assertIn('<input type="radio"   id="female" name="gender" value="Female">', html)
		self.assertIn('<label id="circle">Female</label>', html)
		self.assertIn('<input type="submit" name="submit1" id="submit2" value="Submit">', html)


		self.assertTrue(html.strip().endswith('</html>'))

class ORM_Ko_Toh(TestCase):
	def test_saving_kotoh(self):
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

		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(Item1.today, '2004-04-04')
		self.assertEqual(Item2.org, 'Future Educators Organization')
		self.assertEqual(Item3.username, 'Edmarie L. Suatin')
		self.assertEqual(Item4.batchs, 'BSCE-1A')
		self.assertEqual(Item5.cern, 'TUPC-18-04-05')
		#KulangKoDitoSaORMngRadio

		class Views(TestCase):
	def test_test_lang(self):
		Item.objects.create(today='2004-04-04', 
			org='org', username='username',
			batchs='batchs', cern='cern')
		response = self.client.get('/app/views.Edmarie/')


class ORM_Ko_Toh_Toh(TestCase):
	def test_saving_kotoh(self):
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

		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(Item1.today, '2019-02-05')
		self.assertEqual(Item2.org, 'Engineering Honor Society')
		self.assertEqual(Item3.username, 'Diane Faye S. Tipanao')
		self.assertEqual(Item4.batchs, 'BET-MT-3A')
		self.assertEqual(Item5.cern, 'TUPC-20-02-04')
		#KulangKoDitoSaORMngRadio


class Views(TestCase):
	def test_test_test_lang(self):
		Item.objects.create(today='2019-02-05', 
			org='org', username='username',
			batchs='batchs', cern='cern')
		response = self.client.get('/app/views.Edmarie/')

		#MagGigitCommitAkoDito