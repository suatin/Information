from django.db import models


class Organization(models.Model):
    org_name = models.CharField(max_length=30, default="")
    academic_year = models.CharField(max_length=20, default="")
    adviser = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.org_name


# Office Details
class OfficerDetails(models.Model):
	officer = models.ForeignKey(Organization, default=None, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=20, default="")
	middlename = models.CharField(max_length=20, default="")
	surname = models.CharField(max_length=20, default="")
	contactnumber = models.CharField(max_length=20, default="")
	course_section = models.CharField(max_length=50, default="")
	section = models.CharField(max_length=50, default="")
	gender_choices =(
		('M', 'Male'),
		('F', 'Female'),
		)
	gender_officer = models.CharField(max_length=6,choices=gender_choices)
	emailaddress = models.EmailField(max_length=50, default="")
    #contactnumber = models.EmailField(max_length=50, default="")
	studentIDnumber = models.CharField(max_length=20, default="")
	position = models.CharField(max_length=10, default="")

	def __str__(self):
		return self.name


# Member Details
class MemberDetails(models.Model):
	Member = models.ForeignKey(Organization, default=None, on_delete=models.CASCADE)
	M_firstname = models.CharField(max_length=20, default="")
	M_middlename = models.CharField(max_length=20, default="")
	M_surname = models.CharField(max_length=20, default="")
	M_course_section = models.CharField(max_length=50, default="")
	M_section = models.CharField(max_length=50, default="")
	M_emailaddress = models.EmailField(max_length=50, default="")
	M_contactnumber = models.EmailField(max_length=50, default="")
	M_studentIDnumber = models.CharField(max_length=20, default="")
	gender_choicess =(
        ('M', 'Male'),
        ('F', 'Female'),
        )
	gender_member = models.CharField(max_length=6,choices=gender_choicess)


	def __str__(self):
		return self.M_name

class ActivitiesDetails(models.Model):
	Activities = models.ForeignKey(OfficerDetails, default=None, on_delete=models.CASCADE)
	Poposed_Date = models.DateField(auto_now_add=False, auto_now=False)
	Description_Activities = models.CharField(max_length=50, default="")
    #Proposed Activities
	name_proposed_activities = models.CharField(max_length=20, default="")
	target_paticipant = models.CharField(max_length=20,default="")
	paticipant_number = models.IntegerField(max_length=20,default=0)
	estimated_Budget = models.IntegerField(max_length=20,default=0)

	def __str__(self):
		return self.Poposed_Date


class ReportDetails(models.Model):
	Report = models.ForeignKey(ActivitiesDetails, default=None, on_delete=models.CASCADE)
	Status = models.CharField(max_length=100,default="")
	#Accomplishment_Report = models.FileField(blank=True, Null=True)
	#Overallrating
	Evaluation_Report = models.TextField(max_length=100,default="")
	Description = models.TextField(max_length=100,default="")

	def __str__(self):
		return self.Report