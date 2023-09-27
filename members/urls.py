from django.urls import path
from . import views

urlpatterns = [
	path('members/func',views.func,name='func'),
	path('members/func1',views.func1,name='func1')
]