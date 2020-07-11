from django import forms
from django.contrib.auth.models import User
from . import models 
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
	#username = forms.CharField(label='username',max_length=30,help_text="pas d'espace")
	#email=forms.EmailField(label='email',widget=forms.TextInput(attrs={
	#	'class':'form-control',
	#	'placeholder':'write a email ...'
	#	}))
	#first_name=forms.CharField(label='first_name')
	#last_name=forms.CharField(label='last_name')
	#password1=forms.CharField(label='password1',widget=forms.PasswordInput(),min_length=8)
	#password2=forms.CharField(label='password2',widget=forms.PasswordInput(),min_length=8)
	username = forms.CharField(label='username',max_length=30,help_text="pas d'espace",widget=forms.TextInput(attrs={'class':'c-field u-block',
		
		'placeholder':"Nom d'utilisateur"
		}))
	email=forms.EmailField(label='email',widget=forms.TextInput(attrs={
		'class':'c-field u-block',
		'placeholder':'E-mail'
		}))
	first_name=forms.CharField(label='Nom',widget=forms.TextInput(attrs={'class':'c-field u-block',
		
		'placeholder':'Nom'
		}))
	last_name=forms.CharField(label='Prénom',widget=forms.TextInput(attrs={'class':'c-field u-block',
		
		'placeholder':'Prénom'
		}))
	password1=forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'class':'c-field u-block','placeholder': 'Mot de passe'}),min_length=8)
	password2=forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'class':'c-field u-block','placeholder': 'Répéter le mot de passe'}),min_length=8)
	
	class Meta:
		model = User
		fields =('username','email','first_name','last_name','password1','password2')

	def clean_password2(self):

		cd=self.cleaned_data
		if cd['password1'] != cd['password2']:
			raise forms.ValidationError('password not identical')
		return cd['password2']
	def clean_username(self):
		cd=self.cleaned_data
		if User.objects.filter(username=cd['username']).exists():
			raise forms.ValidationError('user exist')
		return cd['username']

class ProfileForm(forms.ModelForm):
	class Meta:
		model=models.ProfileUser
		fields=['image','country','addres']


class ContactForm(forms.ModelForm):
	class Meta:
		model=models.Contact
		fields=('subject','first_name','last_name','email','countryphone','phone','message')