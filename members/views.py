from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def func(request):
	return HttpResponse("Hello world!")
def func1(request):
	template = loader.get_template('myfirst.html')
	return HttpResponse(template.render())