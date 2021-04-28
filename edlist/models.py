from django.db import models

class Item(models.Model):

	#Date
	today = models.DateTimeField(null=True)
	#Organization
	org = models.CharField(max_length=20, null=True)
	#Name
	username = models.CharField(max_length=20, null=True)
	#Section
	batch = models.CharField(max_length=20, null=True)
	#Student Number
	cern = models.CharField(max_length=500, null=True)
	#GenderTo
	two=(('male', 'gender'),('female','gender'))
	gender = models.CharField(max_length=10, choices=two, default='none')







	def __str__(self):
		return self.org