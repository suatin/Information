from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_browser_First(self):
		self.browser.get(self.live_server_url)
		self.assertIn('TUP-C ACSO', self.browser.title)


		EmText= self.browser.find_element_by_tag_name('h1').text
		self.assertIn('TUP-Cavite Student Organization', EmText)

		form = self.browser.find_element_by_tag_name('form')	

		date = self.browser.find_element_by_id('today').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('today').send_keys("2004-04-04")
		time.sleep(1)

		l1 = self.browser.find_element_by_id('orgs').text
		self.assertIn('Accredited Student Organization:', l1)

		l2 = self.browser.find_element_by_id('usernames').text
		self.assertIn('Full Name:', l2)

		l3 = self.browser.find_element_by_id('batch').text
		self.assertIn('Course:', l3)

		l4 = self.browser.find_element_by_id('concerns').text
		self.assertIn('Student Number:', l4)

		Prg= self.browser.find_element_by_tag_name('p').text
		self.assertIn('Date:', Prg)

		pr2 = self.browser.find_element_by_id('p2').text
		self.assertIn('Gender:', pr2)

		input22 = self.browser.find_element_by_id('org')  
		self.assertEqual(input22.get_attribute('placeholder'),'e.g. University Student Organization')
		input22 = self.browser.find_element_by_id('org').send_keys("Future Educators Organization")
		time.sleep(2)


		input33 = self.browser.find_element_by_id('username')  
		self.assertEqual(input33.get_attribute('placeholder'),'e.g. Lyra F. Eria')
		input33 = self.browser.find_element_by_id('username').send_keys("Edmarie L. Suatin")
		time.sleep(2)


		input44 = self.browser.find_element_by_id('batchs')  
		self.assertEqual(input44.get_attribute('placeholder'),'e.g. BSIE-ICT-3A')
		input44 = self.browser.find_element_by_id('batchs').send_keys("BSCE-1A")
		time.sleep(2)


		input55 = self.browser.find_element_by_id('cern')  
		self.assertEqual(input55.get_attribute('placeholder'),'e.g. TUPC-20-00-00')
		input55 = self.browser.find_element_by_id('cern').send_keys("TUPC-18-04-05")
		time.sleep(2)

		g1 = self.browser.find_element_by_name('gender').click()
		time.sleep(1)

		#g1 = self.browser.find_element_by_name('gender').click()
		#time.sleep(1)

		#m1 = self.browser.find_element_by_id('male').click()
		#time.sleep(1)

		f1 = self.browser.find_element_by_id('female').click()
		time.sleep(1)

		f1 = self.browser.find_element_by_id('female').send_keys("Female")
		time.sleep(1)

		submitbutton = self.browser.find_element_by_name('submit1').click()

		#Nextpage = self.browser.current_url
		#self.assertRegex(Page, '/okay')
		self.browser.quit()	
		#self.browser = webdriver.Firefox()
		#self.browser.get(self.live_server_url)

	def test_browser_second(self):
		self.browser.get(self.live_server_url)	


		EmText= self.browser.find_element_by_tag_name('h1').text
		self.assertIn('TUP-Cavite Student Organization', EmText)

		form = self.browser.find_element_by_tag_name('form')	

		date = self.browser.find_element_by_id('today').click()
		time.sleep(1)
		date = self.browser.find_element_by_id('today').send_keys("2019-02-05")
		time.sleep(1)

		l1 = self.browser.find_element_by_id('orgs').text
		self.assertIn('Accredited Student Organization:', l1)

		l2 = self.browser.find_element_by_id('usernames').text
		self.assertIn('Full Name:', l2)

		l3 = self.browser.find_element_by_id('batch').text
		self.assertIn('Course:', l3)

		l4 = self.browser.find_element_by_id('concerns').text
		self.assertIn('Student Number:', l4)

		Prg= self.browser.find_element_by_tag_name('p').text
		self.assertIn('Date:', Prg)

		pr2 = self.browser.find_element_by_id('p2').text
		self.assertIn('Gender:', pr2)

		input22 = self.browser.find_element_by_id('org')  
		self.assertEqual(input22.get_attribute('placeholder'),'e.g. University Student Organization')
		input22 = self.browser.find_element_by_id('org').send_keys("Engineering Honor Society")
		time.sleep(2)


		input33 = self.browser.find_element_by_id('username')  
		self.assertEqual(input33.get_attribute('placeholder'),'e.g. Lyra F. Eria')
		input33 = self.browser.find_element_by_id('username').send_keys("Diane Faye S. Tipanao")
		time.sleep(2)


		input44 = self.browser.find_element_by_id('batchs')  
		self.assertEqual(input44.get_attribute('placeholder'),'e.g. BSIE-ICT-3A')
		input44 = self.browser.find_element_by_id('batchs').send_keys("BET-MT-3A")
		time.sleep(2)


		input55 = self.browser.find_element_by_id('cern')  
		self.assertEqual(input55.get_attribute('placeholder'),'e.g. TUPC-20-00-00')
		input55 = self.browser.find_element_by_id('cern').send_keys("TUPC-20-02-04")
		time.sleep(2)

		g1 = self.browser.find_element_by_name('gender').click()
		time.sleep(1)

		#g1 = self.browser.find_element_by_name('gender').click()
		#time.sleep(1)

		m1 = self.browser.find_element_by_id('male').click()
		time.sleep(1)

		m1 = self.browser.find_element_by_id('male').send_keys("Male")
		time.sleep(1)

		submitbutton = self.browser.find_element_by_name('submit1').click()
		time.sleep(2)


		#Nextpage = self.browser.current_url
	def Edmarie(self):
		#self.assertRegex(Page, '/okay')
		self.browser.quit()	

# if __name__ == '__main__':
#	unittest.main()