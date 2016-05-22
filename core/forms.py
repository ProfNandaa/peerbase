from django import forms

class userForm(forms.Form):
	full_name = forms.CharField(label='first name', min_length=3, max_length=100)
	email = forms.CharField(label='email', max_length=100, min_length=3)
	password = forms.CharField(label='email', min_length=6, max_length=50)


def save(self, data):
	u = User.objects.create_user(data['full_name'],
								data['email'],
								data['password'])
	return u