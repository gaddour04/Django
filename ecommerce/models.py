from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	cat=models.CharField(max_length=100,verbose_name=_("Category"))
	#catparent=models.ForeignKey('self', limit_choices_to={'catparent__isnull' : True}, on_delete=models.CASCADE,blank=True ,null=True,verbose_name=_("Category Parent"))
	desc=models.TextField(verbose_name=_("Description"))
	#catimg=models.ImageField(upload_to='category/',verbose_name=_("Image"))

	def __str__(self):
		return self.cat

class Marque(models.Model):
	marque=models.CharField(max_length=100,verbose_name=_("Marque"))
	desc=models.TextField(verbose_name=_("Description"))
	

	def __str__(self):
		return self.marque

class Forme(models.Model):
	forme=models.CharField(max_length=100,verbose_name=_("Forme"))
	desc=models.TextField(verbose_name=_("Description"))
	
	def __str__(self):
		return self.forme

class Genre(models.Model):
	genre=models.CharField(max_length=100,verbose_name=_("Genre"))
	
	
	def __str__(self):
		return self.genre

class Style(models.Model):
	style=models.CharField(max_length=100,verbose_name=_("Style"))
	
	
	def __str__(self):
		return self.style
class Matière(models.Model):
	matière=models.CharField(max_length=100,verbose_name=_("Matière"))
	def __str__(self):
		return self.matière

class Product(models.Model):
	Color=(
					('red','red'),
					('black','black'),
					('goldenrod','goldenrod'),
					('pink','pink')
					)
	name=models.CharField(max_length=100, verbose_name=_("Name"))
	category=models.ForeignKey(Category,on_delete=models.CASCADE , blank=True, null=True, verbose_name=_("Category"))
	marque=models.ForeignKey(Marque,on_delete=models.CASCADE , blank=True, null=True, verbose_name=_("Marque"))
	forme=models.ForeignKey(Forme,on_delete=models.CASCADE , blank=True, null=True, verbose_name=_("Forme"))
	#brand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Brand"))
	desc=models.TextField(verbose_name=_("Description"))
	genre=models.ForeignKey(Genre,on_delete=models.CASCADE , blank=True, null=True, verbose_name=_("Genre"))
	style=models.ForeignKey(Style,on_delete=models.CASCADE , blank=True, null=True, verbose_name=_("Style"))
	matière=models.ForeignKey(Matière,on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("Matière"))
	colorr=models.CharField(choices=Color,max_length=100, verbose_name=_("colorr "),blank=True,null=True)
	image1=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 1"))
	image2=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 2"))
	image3=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 3"))
	color2=models.BooleanField(default=False , verbose_name=_("Color 2"))
	colorrr=models.CharField(choices=Color,max_length=100, verbose_name=_("colorr "),blank=True,null=True)
	image4=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 1"))
	image5=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 2"))
	image6=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 3"))
	color3=models.BooleanField(default=False , verbose_name=_("Color 3"))
	colorrrr=models.CharField(choices=Color,max_length=100, verbose_name=_("colorrr "),blank=True,null=True)
	image7=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 1"))
	image8=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 2"))
	image9=models.ImageField(upload_to='product/',blank=True,null=True, verbose_name=_("Image 3"))
	price=models.DecimalField(max_digits=5, decimal_places=2,verbose_name=_("Price"))
	discountprice=models.DecimalField(max_digits=5, decimal_places=2,verbose_name=_("Discount Price"))
	cost=models.DecimalField(max_digits=5 ,decimal_places=2,verbose_name=_("Cost"))
	created=models.DateTimeField(verbose_name=_("Created"))

	slug=models.SlugField(blank=True,null=True, verbose_name=_("Slug"))
	prodIsNew=models.BooleanField(default=True , verbose_name=_("Is New"))
	prodBestSeller=models.BooleanField(default=False, verbose_name=_("Best Seller"))

	#favourite = models.ManyToManyField(User,related_name='favourite',default=None ,blank=True,null=True)

	
	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):

		self.slug=slugify(self.name)
		super(Product,self).save(*args,**kwargs)

	####### kan el slug mech mawjoud wana zedtou baad fel models ####
	#def save(self ,*args,**kwargs):
	#	if not self.slug:
	#		self.slug=slugify(self.name)
	#		super(Product,self).save(*args,**kwargs)
	#	else:
	#		super(Product,self).save(*args,**kwargs)


	####### bech ihezni el page el detail maa el slug ###
	def get_absolute_url(self):
		return reverse('products:product_detail', kwargs={'slug':self.slug,'colorr':self.colorr})

	def get_absolute_url_color(self):
		return reverse('products:product_detail1', kwargs={'slug':self.slug,'colorrr':self.colorrr})
	
		