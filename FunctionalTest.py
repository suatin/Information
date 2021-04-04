from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		#self.browser.maximize_window()

	'''def tearDown(self):
		self.browser.close()
		self.browser.quit()
		print("Tapos na ang testing natin")'''

		

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Page Title', self.browser.title)

		#H1
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('University Student Government', headerText)

		#select
		select = self.browser.find_element_by_id('org').send_keys('FUTURE EDUCATORS ORGANIZATIONS')
		time.sleep(2)


		#select
		select = self.browser.find_element_by_id('org').click()
		time.sleep(2)

		label1 = self.browser.find_element_by_id('username').text
		self.assertIn('Full Name:', label1)
		firstname = self.browser.find_element_by_name('username').send_keys("Edmarie L. Suatin")
		time.sleep(2)

		#username
		label1 = self.browser.find_element_by_id('batch').text
		self.assertIn('Course:', label1)
		course = self.browser.find_element_by_name('batch').send_keys("BSIE-ICT")
		time.sleep(2)
		#submit mo lang
		button = self.browser.find_element_by_id('coc').click()
		time.sleep(2)


		


if __name__ == '__main__':
	unittest.main()

