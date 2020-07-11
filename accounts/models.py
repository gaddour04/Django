from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
import datetime
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from phone_field import PhoneField
from django_countries.fields import CountryField



class ProfileUser(models.Model):

	user=models.OneToOneField(User,verbose_name=_("user"), on_delete=models.CASCADE)

	slug=models.SlugField(blank=True,null=True)

	image=models.ImageField(default="user-par-default.png",verbose_name=_("Image"),upload_to='profile_img',blank=True,null=True)

	addres=models.CharField(max_length=100)

	country = CountryField()

	join_date =models.DateTimeField(verbose_name=_("Join date"),default=datetime.datetime.now)

	def save(self ,*args,**kwargs):
		if not self.slug:
			self.slug=slugify(self.user.username)
			super(ProfileUser,self).save(*args,**kwargs)

	



	class Meta:
		verbose_name=_("Profile")
		verbose_name_plural=_("Profiles")

	def __str__(self):
		return '%s' %(self.user)  #kima str

	def get_absolute_url(sefl):
		return reverse("accounts:Profile_detail",kwargs={"slug":self.slug})


def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile=ProfileUser.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)


class Contact(models.Model):
	'''STATUS=(
					('Achat en ligne','Achat en ligne'),
					('Information sur nos produits','Information sur nos produits'),
					choices=STATUS,)'''
	subject=models.CharField(max_length=50, blank=True,null=True)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	countryphone=models.CharField(max_length=50,blank=True,null=True)
	phone =models.IntegerField(blank=True,null=True)
	message=models.TextField()

	def __str__(self):
		return f'{self.first_name} {self.last_name}'