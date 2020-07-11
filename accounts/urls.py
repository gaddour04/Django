from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name='accounts'

urlpatterns = [


   
    path('signup',views.signup,name='signup'),
    path('profile/<slug:slug>',views.profile,name='profile'),
    path('contact',views.contact,name='contact')
    
    

]