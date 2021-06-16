from django.urls import path
from . import views

urlpatterns = [
	#path('', views.admin)
	path('', views.home),
	path('home.html', views.home),
	path('organization.html', views.org, name="organization.html"),
	path('dual.html', views.member, name="dual.html"),
	path('activities.html', views.officer, name="activities.html"),
	path('reports.html', views.report, name="reports.html"),
	path('display.html', views.play, name="display.html"),

]