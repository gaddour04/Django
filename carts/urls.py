from django.urls import path
from . import views

app_name='carts'

urlpatterns = [


   
    path('view',views.view,name='view'),
    path('view/<slug:slug>/',views.update_cart,name='update_cart'),
    path('view1/<slug:slug>/',views.remove_cart,name='remove_cart'),
    

    
    
    

]