from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import RegisterForm

# Create your views here.

def index(request):
	return render(request, 'core/index.html')

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		data = {}
		fullname = form.cleaned_data['name'].split()
		data['first_name'] = fullname[0]
		data['last_name'] = fullname[1]
		data['email']=form.cleaned_data['email']
		data['password']=form.cleaned_data['password']
		form = registerForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/Thank you!/')
	else:
		form = registerForm()

		form.save(data)
		request.session['registered']=True

	return render(request, 'core/register.html')

def login(request):
	return render(request, 'core/login.html')
