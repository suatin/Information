from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http:/127.0.0.1:8000')

'''
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		#self.browser.maximize_window()

	def tearDown(self):
		self.browser.close()
		self.browser.quit()
		print("Finally, Thank you Lord)

		

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('ACSO', self.browser.title)

		#H1
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('University Student Government', headerText)

		#Select
		select = self.browser.find_element_by_id('org').send_keys('FUTURE EDUCATORS ORGANIZATIONS')
		time.sleep(2)

		#Select
		select = self.browser.find_element_by_id('org').click()
		time.sleep(2)




		label1 = self.browser.find_element_by_id('username').text
		self.assertIn('Full Name:', label1)
		Fullname = self.browser.find_element_by_name('username').send_keys("Edmarie L. Suatin")
		time.sleep(2)
  	

		#Firstname MI. Surname
		label1 = self.browser.find_element_by_id('batch').text
		self.assertIn('Course:', label1)
		course = self.browser.find_element_by_name('batch').send_keys("BSIE-ICT")
		time.sleep(2)

		#Finally
		button = self.browser.find_element_by_id('coc').click()
		time.sleep(2)

	#	headerText = self.browser.find_element_by_tag_name('p').text
	#	self.assertIn('University Student Government', headerText)
	#	AssertionError: 'University Student Government' not found in 'List of Accreditted Student Organization 2020-2021'


	#	H1
	#	headerText = self.browser.find_element_by_tag_name('h1').text
	#	self.assertIn('University Student Government', headerText)
	#   self.assertIn('University Student Government' headerText)
    #	SyntaxError: invalid syntax


	#	label1 = self.browser.find_element_by_id('username').text
	#	self.assertIn('Full Name:', label1)
	#	firstname = self.browser.find_element_by_name('username').send_keys("Edmarie L. Suatin")
	#	time.sleep(2)
  	

	#	Select
	#	select = self.browser.find_element_by_id('org').send_keys('FUTURE EDUCATORS ORGANIZATIONS')
	#	time.sleep(2)
	#	select = selfbrowser.find_element_by_id('org').send_keys('FUTURE EDUCATORS ORGANIZATIONS')
	#	NameError: name 'selfbrowser' is not defined

	#	if _name__ == '__main__':
	#	NameError: name '_name__' is not defined


if __name__ == '__main__':
	unittest.main()
'''
