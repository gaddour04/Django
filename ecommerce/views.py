from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from .models import Product
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.db.models.functions import Coalesce

# Create your views here.
def index1(request):
	data=models.produit.objects.all()
	return render(request,'tejrab1.html',{'d':data})
def tejrab(request):
	new=models.Product.objects.all().filter(prodIsNew=True)[:12]
	context={'new':new}

	return render(request,'index.html',context)
def shop(request):
	return render(request,'product-page.html',{})
def single(request):
	return render(request,'detail-page.html',{})
def check(request):
	return render(request,'checkout.html',{})

def search(request):
	try:
		keywords =request.GET.get('keywords')
	except:
		keywords = None
	if keywords:
		product_list=models.Product.objects.filter(name__icontains=keywords)
		myFilter=ProductFilter(request.GET,product_list)
		abc=product_list.count()
		context={'query':keywords ,'product_list':product_list,'myFilter':myFilter,'abc':abc}
		template='search.html'
	else:
		template ='femme-product.html'
		context={}

	
	return render(request , template,context)



def product_list_femme(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=Product.objects.filter(genre='2',category='2') #femme , soleil
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	abc=product_list.count()
	



	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)


	
	context={'product_list':product_list,'myFilter':myFilter,'abc':abc}
	return render(request , 'femme-product.html',context)

def product_list_homme(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=Product.objects.filter(genre='1',category='2')
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	



	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)


	
	context={'product_list':product_list,'myFilter':myFilter}
	return render(request , 'homme-product.html',context)

def product_list_price_desc(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=models.Product.objects.all()
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	
	
	#abc=models.Product.objects.order_by(Coalesce('price', 'name').desc())
	abc=Product.objects.filter(genre='2',price__gte='200', price__lte='300').order_by(Coalesce('price', 'name').asc())
	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)	
	context={'abc':abc,'myFilter':myFilter}
	return render(request , 'price200-300.html',context)
def product_list_price_desc1(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=models.Product.objects.all()
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	
	
	#abc=models.Product.objects.order_by(Coalesce('price', 'name').desc())
	abc=Product.objects.filter(genre='2',price__gte='300', price__lte='400').order_by(Coalesce('price', 'name').asc())
	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)	
	context={'abc':abc,'myFilter':myFilter}
	return render(request , 'price300-400.html',context)

def product_list_price_desc2(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=models.Product.objects.all()
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	
	
	#abc=models.Product.objects.order_by(Coalesce('price', 'name').desc())
	abc=Product.objects.filter(genre='2',price__gte='400', price__lte='500').order_by(Coalesce('price', 'name').asc())
	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)	
	context={'abc':abc,'myFilter':myFilter}
	return render(request , 'price400-500.html',context)

def product_detail(request,slug,colorr):
	#product_detail=models.Product.objects.get(slug=slug)
	product_detail=get_object_or_404(Product,slug=slug,colorr=colorr)
	'''is_favourite =False
				if product_detail.favourite.filter(id=request.user.id).exists():
					is_favourite=True'''
	new=models.Product.objects.all().filter(prodIsNew=True)[:12]
	print(new)
	context={'product_detail':product_detail,'new':new}
	return render(request,'detail-page.html',context)

def product_detail1(request,slug,colorrr):
	#product_detail=models.Product.objects.get(slug=slug)
	product_detail=get_object_or_404(Product,slug=slug,colorrr=colorrr)
	'''is_favourite =False
				if product_detail.favourite.filter(id=request.user.id).exists():
					is_favourite=True'''
	new=models.Product.objects.all().filter(prodIsNew=True)[:12]
	context={'product_detail':product_detail,'new':new}
	return render(request,'detail1-page.html',context)


'''def product_favourite(request,slug):
	product_detail=get.get_object_or_404(Product,slug=slug)
	if product_detail.favourite.filter(id=request.user.id).exists():
		product_detail.favourite.remove(request.user)
	else :
		product_detail.favourite.add(request.user)
	return HttpResponseRedirect('product_detail')

def product_favourite_list(request):
	user =request.user
	favourite_product = user.favourite.all()
	context={
	'favourite_product':favourite_product
	}
	return render (request,'favoris.html',context)'''


##############################lunette de vue ####################

def product_list_femme_vue(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=Product.objects.filter(genre='2',category='1') #femme , soleil
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	



	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)


	
	context={'product_list':product_list,'myFilter':myFilter}
	return render(request , 'femme-product-vue.html',context)

def product_list_homme_vue(request):
	key=request.session.session_key
	print(key)
	#request.session.set_expiry(30)
	product_list=Product.objects.filter(genre='1',category='1') #femme , soleil
	myFilter=ProductFilter(request.GET,product_list)
	product_list=myFilter.qs
	



	paginator = Paginator(product_list, 12) # Show 4 contacts per page.
	page = request.GET.get('page')
	product_list = paginator.get_page(page)


	
	context={'product_list':product_list,'myFilter':myFilter}
	return render(request , 'homme-product-vue.html',context)


def navbar(request):
	return render(request,'navbarjdida.html',{})