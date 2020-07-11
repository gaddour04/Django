from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth import login , authenticate
from . forms import UserForm,ProfileForm,ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .models import ProfileUser , Contact
from . import models
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def signup(request):
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password1'])
			new_user.save()
			
			#username = form.cleaned_data['username']
			messages.success(request,'success {}'.format(new_user)) #django version < 3.6
			#messages.success(request,f'success {username}') django version > 3.6
			return redirect('login')

	else:
		form=UserForm()

	context = {'form':form}

	return render(request,'registration/signup.html',context)
	
@login_required(login_url='login')
def profile(request,slug):
	profile=get_object_or_404(ProfileUser,slug=slug)
	context={'profile':profile}
	return render (request,'profile.html',context)

#def profile(request):
	#profile=get_object_or_404(ProfileUser,slug=slug)
#	profile_form=ProfileForm()
#	return render (request,'profile.html',{'profile_form':profile_form})


def contact(request):
	if request.method == 'POST':

		form=ContactForm(request.POST)
		if form.is_valid():
			subject=form.cleaned_data["subject"]
			form.cleaned_data["first_name"]
			form.cleaned_data["last_name"]
			sender=[settings.EMAIL_HOST_USER]
			to=form.cleaned_data["email"]
			message=form.cleaned_data["message"]
			phone=form.cleaned_data["phone"]
			countryphone=form.cleaned_data["countryphone"]
			
			form.save()
			send_mail(subject,message + ' ' + to,to,sender,fail_silently=True)
			send_mail('bienvenue','ahla bik',settings.EMAIL_HOST_USER,[to],fail_silently=True)
			return HttpResponseRedirect('contact')
	else:
		form=ContactForm()
	'''if request.method == 'POST':
					subject=request.POST['subject']
					first_name=request.POST['first_name'] #eli fel [] hia name mta3 el input
					last_name=request.POST['last_name']
					email=request.POST['email']
					countryphone=request.POST['countryphone']
					phone=request.POST['phone']
					message=request.POST['message']
			
					send_mail(
						'message from ' + email  , #subject
						message + '  '+ email , 								   #message
						email,                                     #from email
						[settings.EMAIL_HOST_USER],                   # to email		         
						fail_silently=False )




		# thot action fel form wala tzid adha 
		new_mail=models.Contact()
								new_mail.first_name=first_name
								new_mail.last_name=last_name
								new_mail.email=email
								new_mail.message=message
								new_mail.save()'''
								



	return render (request,'contact.html',{'form':form})