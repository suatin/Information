from django.urls import path
from . import views

urlpatterns = [
	path('', views.Main1),
	path('Contibute', views.Page, name="Contibute"),
]