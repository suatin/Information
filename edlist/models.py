from django.db import models



class Mainpage(models.Model):
	organization = models.CharField(max_length=10, default='none')
	one=(('position', 'officer'),('position','member'))
	position = models.CharField(max_length=10, choices=one, default='none')

	def __str__(self):
		return self.organization


class Officer(models.Model):
	Officer = models.ForeignKey(Mainpage, default=None, on_delete=models.CASCADE, null=True)
	firstname = models.CharField(max_length=20, null=True)
	middle = models.CharField(max_length=500, null=True)
	surname = models.CharField(max_length=500, null=True)
	course = models.CharField(max_length=500, null=True)
	section = models.CharField(max_length=500, null=True)
	number= models.CharField(max_length=500, null=True)
	email = models.TextField (max_length=500, null=True)
	position = models.CharField(max_length=500, null=True)
	two=(('male', 'gender'),('female','gender'),('others','gender'))
	gender = models.CharField(max_length=10, choices=two, default='none')
	today = models.DateTimeField(null=True)
	#option = models.ManyToManyField(Mainpage)

	def __str__(self):
		return self.Officer


class Member(models.Model):
	Member = models.ForeignKey(Mainpage, default=None, on_delete=models.CASCADE, null=True)
	firstname2 = models.CharField(max_length=50, null=True)
	middle2 = models.CharField(max_length=10, null=True)
	surname2 = models.CharField(max_length=50, null=True)
	course2 = models.CharField(max_length=100, null=True)
	section2 = models.CharField(max_length=100, null=True)
	email2 = models.TextField(max_length=100, null=True)
	number2 = models.CharField(max_length=100, null=True)
	two=(('male', 'gender'),('female','gender'),('others','gender'))
	gender2 = models.CharField(max_length=10, choices=two, default='none')
	today2 = models.DateTimeField(null=True)
	#option = models.ManyToManyField(Mainpage)

	def __str__(self):
		return self.Member

class Contribute(models.Model):
	Contribution = models.ManyToManyField(Mainpage)
	date = models.DateTimeField(null=True)

	def __str__(self):
		return self.Contribution


class Contribution2(models.Model):
	Contribution2 = models.ManyToManyField(Mainpage)
	fees = models.CharField(max_length=300, null=True)
	display = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.Contribution2

class Activities(models.Model):
	Activities1 = models.ManyToManyField(Mainpage)
	Adviser = models.CharField(max_length=300, null=True)
	Aone = models.CharField(max_length=100, null=True)
	Atwo = models.CharField(max_length=100, null=True)
	Athree = models.CharField(max_length=100, null=True)
	Afour = models.CharField(max_length=100, null=True)
	Afive = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.Activities

class ActivitiesDisplay(models.Model):
	ActivitiesDisplay1 = models.ManyToManyField(Mainpage)
	Adate = models.DateTimeField(null=True)
	ASuggestion = models.CharField(max_length=100, null=True)
	AComments = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.ActivitiesDisplay

class survey(models.Model):
	Sstrength = models.CharField(max_length=500, null=True)
	Sweak = models.CharField(max_length=500, null=True)
	SSuggestion = models.CharField(max_length=500, null=True)
	SFeedback = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.strength



'''
class Mainpage(models.Model):
	organization = models.CharField(max_length=10, default='none')

	def __str__(self):
		return self.organization

class Officer(models.Model):
	Officer = models.ForeignKey(Mainpage, default=None, on_delete=models.CASCADE, null=True)
	firstname = models.CharField(max_length=20, null=True)
	middle = models.CharField(max_length=500, null=True)
	surname = models.CharField(max_length=500, null=True)
	course = models.CharField(max_length=500, null=True)
	section = models.CharField(max_length=500, null=True)
	number= models.CharField(max_length=500, null=True)
	email = models.TextField (max_length=500, null=True)
	position = models.CharField(max_length=500, null=True)
	two=(('male', 'gender'),('female','gender'))
	gender = models.CharField(max_length=10, choices=two, default='none')
	today = models.DateTimeField(null=True)
	option = models.ManyToManyField(Mainpage)

	def __str__(self):
		return self.Officer



class Mainpage(models.Model):
	organization = models.CharField(max_length=10, default='none')
	Oone=(('officer1', 'position'),('member','position'))
	Oposition = models.CharField(max_length=10, choices=Oone, default='none')

	def __str__(self):
		return self.organization

class Officerchoice(models.Model):
	Officer = models.ForeignKey(Mainpage, default=None, on_delete=models.CASCADE, null=True)
	firstname = models.CharField(max_length=20, null=True)
	middle = models.CharField(max_length=500, null=True)
	surname = models.CharField(max_length=500, null=True)
	course = models.CharField(max_length=500, null=True)
	section = models.CharField(max_length=500, null=True)
	number= models.CharField(max_length=500, null=True)
	email = models.TextField (max_length=500, null=True)
	position = models.CharField(max_length=500, null=True)
	two=(('male', 'gender'),('female','gender'))
	gender = models.CharField(max_length=10, choices=two, default='none')
	today = models.DateTimeField(null=True)
	option = models.ManyToManyField(Mainpage)

	def __str__(self):
		return self.Officer

class Memberchoice(models.Model):
	Member = models.ForeignKey(Mainpage, default=None, on_delete=models.CASCADE, null=True)
	firstname2 = models.CharField(max_length=50, null=True)
	middle2 = models.CharField(max_length=10, null=True)
	surname2 = models.CharField(max_length=50, null=True)
	course2 = models.CharField(max_length=100, null=True)
	section2 = models.CharField(max_length=100, null=True)
	email2 = models.TextField(max_length=100, null=True)
	number2 = models.CharField(max_length=100, null=True)
	three=(('male', 'gender'),('female','gender'))
	gender2 = models.CharField(max_length=10, choices=three, default='none')
	today2 = models.DateTimeField(null=True)
	option = models.ManyToManyField(Mainpage)


	def __str__(self):
		return self.Member

class Contribute(models.Model):
	Contribution = models.ManyToManyField(Mainpage)
	date = models.DateTimeField(null=True)

	def __str__(self):
		return self.Contribution


class Contribution2(models.Model):
	Contribution2 = models.ManyToManyField(Mainpage)
	Mdate = models.DateTimeField(null=True)

	def __str__(self):
		return self.Contribution2

class Activities(models.Model):
	Activities1 = models.ManyToManyField(Mainpage)
	Adviser = models.CharField(max_length=300, null=True)
	Aone = models.CharField(max_length=100, null=True)
	Atwo = models.CharField(max_length=100, null=True)
	Athree = models.CharField(max_length=100, null=True)
	Afour = models.CharField(max_length=100, null=True)
	Afive = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.Activities1

class ActivitiesDisplay(models.Model):
	ActivitiesDisplay1 = models.ManyToManyField(Mainpage)
	Adate = models.DateTimeField(null=True)
	ASuggestion = models.CharField(max_length=100, null=True)
	AComments = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.ActivitiesDisplay1

class survey(models.Model):
	Sstrength = models.CharField(max_length=500, null=True)
	Sweak = models.CharField(max_length=500, null=True)
	SSuggestion = models.CharField(max_length=500, null=True)
	SFeedback = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.Sstrength'''


