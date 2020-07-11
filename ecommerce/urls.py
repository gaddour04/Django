from django.urls import path
from . import views

app_name='products'

urlpatterns = [


   
   
    #path('tejrab',index1),
    path('index',views.tejrab,name='tejrab'),
    #path('shop/',views.shop,name='shop'),
    path('single/',views.single,name='single'),
    path('femme/lunette-de-soleil/',views.product_list_femme,name='product_list'),
    path('homme/lunette-de-soleil/',views.product_list_homme,name='product_list_homme'),
    path('femme/lunette-de-vue/',views.product_list_femme_vue,name='product_list_vue'),
    path('homme/lunette-de-vue/',views.product_list_homme_vue,name='product_list_home_vue'),

    path('femme/price-200-300/',views.product_list_price_desc,name='product_list_price_desc'),
    path('femme/price-300-400/',views.product_list_price_desc1,name='product_list_price_desc1'),
    path('femme/price-400-500/',views.product_list_price_desc2,name='product_list_price_desc2'),
    path('<slug:slug>/color-<str:colorr>',views.product_detail,name='product_detail'),
    path('<slug:slug>/color1-<str:colorrr>',views.product_detail1,name='product_detail1'),
    
   #path('<slug:slug>',views.product_favourite,name='product_favourite'),
    #path('product_favourite_list/',views.product_favourite_list,name='product_favourite_list'),
    path('check/',views.check,name='check'),
    path('search/',views.search,name='search'),
    path('navbar/',views.navbar,name='navbar'),
    
    
    
    

]









