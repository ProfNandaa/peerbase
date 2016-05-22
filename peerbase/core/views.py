from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'core/index.html')

def register(request):
	return render(request, 'core/register.html')

def login(request):
	return render(request, 'core/login.html')
