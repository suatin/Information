from django.contrib import admin
from .models import Organization, OfficerDetails, MemberDetails, ReportDetails, ActivitiesDetails

admin.site.register(Organization)
admin.site.register(OfficerDetails)
admin.site.register(ActivitiesDetails)
admin.site.register(ReportDetails)
admin.site.register(MemberDetails)

# Register yoxzur models here.
