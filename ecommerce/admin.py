from django.contrib import admin

# Register your models here.
from .models import Product,Category,Forme,Marque,Genre,Style,Matière


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','category', 'colorr', 'marque', 'genre', 'style' ,'price' )
admin.site.register(Product,ProductAdmin)

admin.site.register(Category)
admin.site.register(Marque)
admin.site.register(Forme)
admin.site.register(Genre)
admin.site.register(Style)
admin.site.register(Matière)
