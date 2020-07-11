"""lunette URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from ecommerce.views import index1,tejrab,shop,single
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('ecommerce.urls',namespace='products')),
     path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('carts/', include('django.contrib.auth.urls')),
    path('carts/',include('carts.urls',namespace='carts')),
    #path('oauth/', include('social_django.urls', namespace='social')),
    path('social-auth/', include('social_django.urls', namespace='social'))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
