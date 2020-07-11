import django_filters
from .models import Product
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
	#name= CharFilter(field_name='name',lookup_expr='icontains')
	class Meta:
		model = Product
		fields= ('marque','forme','style')
		#fields= ('category','marque','forme','style','price')