from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from forms import userForm

# Create your views here.

def index(request):
	return render(request, 'core/index.html')

def register(request):
	if request.user.is_authenticated():
		return redirect(home)
	if request.method == 'POST':
		import pdb; pdb.set_trace();
		form = UserForm(request.POST)
		if form.is_valid():
			data = {}
			fullname = form.cleaned_data['name'].split()
			data['first_name'] = fullname[0]
			data['last_name'] = fullname[1]
			data['email']=form.cleaned_data['email']
			data['password']=form.cleaned_data['password']

			form.save(data)# Saves the user

			request.session['registered']=True # For display purpose
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
