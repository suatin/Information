from django.contrib import admin
from django.urls import path, include



urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('edlist.urls')),
] 
'''
urlpatterns = [
	#path('', views.admin)
	path('home.html', views.home, name="home.html"),
	path('organization.html', views.org, name="organization.html"),
	path('dual.html', views.member, name="dual.html"),
	path('activities.html', views.officer, name="activities.html"),
	path('reports.html', views.report, name="reports.html"),
	path('display.html', views.play, name="display.html"),

]'''