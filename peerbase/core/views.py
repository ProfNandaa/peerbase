from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'core/index.html')

def register(request):
	return render(request, 'core/register.html')

def login(request):
	return render(request, 'core/login.html')

def user_dashboard(request):
	# dammy data
	uploads = []
	for i in range(1, 11):
		upload = {
			'title': 'Sample Upload ' + str(i),
			'files': i + 4,
			'size': (i + 4) * 64,
			'seed': 4,
			'leech': 2
		}
		uploads.append(upload)
		
	data = {
		'uploads': uploads
	}
	return render(request, 'core/user_dashboard.html', data)
