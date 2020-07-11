from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from .models import Cart ,CartItem
from ecommerce.models import Product
from .forms import QauntityForm


# Create your views here.

#def view(request):
#	cart=Cart.objects.all()[0]
#	context = {'cart':cart}
#	return render(request,'cart.html',context)



def view(request):
	'''if request.method == 'POST':
					form=QauntityForm(request.POST)
					if form.is_valid():
						form.save()
				else:
					form=QauntityForm()'''
	


	request.session['user'] = request.user.username
	try:
		the_id =request.session['cart_id01']
	except:
		the_id =None
	if the_id :
		new=Product.objects.all().filter(prodBestSeller=True)[:12]
		cart=Cart.objects.get(id=the_id)
		context ={'cart':cart,'new':new}
	else:
		empty_message = "Votre panier ne contient pour l’instant aucun article"
		context={'empty':True , "empty_message":empty_message}
	return render(request,'cart.html',context)



def update_cart(request,slug):
	request.session.set_expiry(120000000)
	try:
		the_id = request.session['cart_id01']
	except:
		new_cart =Cart()
		new_cart.save()
		request.session['cart_id01'] = new_cart.id
		the_id = new_cart.id
	cart = Cart.objects.get(id=the_id)

	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	cart_item,created = CartItem.objects.get_or_create(cart = cart,product=product)
	if not cart_item in cart.cartitem_set.all(): # si l'article mech fel cart 
		if cart_item.product.discountprice > 0 :

			cart_item.line_total=float(cart_item.product.discountprice) * cart_item.quantity
		else:
			cart_item.line_total=float(cart_item.product.price) * cart_item.quantity
		cart_item.quantity =1
		
		cart_item.save()
		cart.cartitem_set.add(cart_item)



	else:
		cart_item.quantity +=1
		if cart_item.product.discountprice > 0 :

			cart_item.line_total=float(cart_item.product.discountprice) * cart_item.quantity
		else:
			cart_item.line_total=float(cart_item.product.price) * cart_item.quantity
		cart_item.save()


	
	new_total=0.00

	for item in cart.cartitem_set.all():
		if item.product.discountprice > 0 :
			line_total=float(item.product.discountprice) * item.quantity

			new_total += line_total
		else :
			line_total=float(item.product.price) * item.quantity
			new_total += line_total

	cart.total=new_total

	request.session['items_total']=cart.cartitem_set.count()
	if request.session['items_total']  in (0,1):
		red=0
	elif request.session['items_total'] ==2:
		red=((cart.total*5)/100)
	elif request.session['items_total'] ==3:
		red=((cart.total*10)/100)
	elif request.session['items_total'] ==4:
		red=((cart.total*15)/100)
	elif request.session['items_total'] ==5:
		red=((cart.total*20)/100)
	else:
		red=((cart.total*25)/100)
	cart.reduction=red

	
	cart.total=new_total
	cart.totalf=cart.total - cart.reduction
	cart.save()
#########################
	return HttpResponseRedirect('/carts/view')


#def update_cart(request,slug):
#	cart=Cart.objects.all()[0]
#	try:
#		product=Product.objects.get(slug=slug)
#	except Product.DoesNotExist:
#		pass
#	except:
#		pass
#	if not product in cart.products.all():
#		cart.products.add(product)
#	else:
#		cart.products.remove(product)


####### total #######
#	new_total=0.00
#	for item in cart.products.all():
#		new_total += float(item.price)
#	cart.total=new_total
#	cart.save()
#########################
#	return HttpResponseRedirect('/carts/view')
def remove_cart(request,slug):
	request.session.set_expiry(120000000)
	try:
		the_id = request.session['cart_id01']
	except:
		new_cart =Cart()
		new_cart.save()
		request.session['cart_id01'] = new_cart.id
		the_id = new_cart.id
	cart = Cart.objects.get(id=the_id)

	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	cart_item,created = CartItem.objects.get_or_create(cart=cart,product=product)
	if  cart_item in cart.cartitem_set.all(): # si l'article mech fel cart 
		cart_item.quantity=0
		cart_item.save()
		cart.cartitem_set.remove(cart_item)
		
		
	
	new_total=0.00

	for item in cart.cartitem_set.all():
		if item.product.discountprice > 0 :
			line_total=float(item.product.discountprice) * item.quantity

			new_total += line_total
		else :
			line_total=float(item.product.price) * item.quantity
			new_total += line_total
	cart.total=new_total
	request.session['items_total']=cart.cartitem_set.count()
	if request.session['items_total']  in (0,1):
		red=0
	elif request.session['items_total'] ==2:
		red=((cart.total*5)/100)
	elif request.session['items_total'] ==3:
		red=((cart.total*10)/100)
	elif request.session['items_total'] ==4:
		red=((cart.total*15)/100)
	elif request.session['items_total'] ==5:
		red=((cart.total*20)/100)
	else:
		red=((cart.total*25)/100)
	cart.reduction=red

	
	
	cart.totalf=cart.total - cart.reduction
	cart.save()
#########################
	return HttpResponseRedirect('/carts/view')
