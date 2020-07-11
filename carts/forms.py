from django import forms

from .models import CartItem

class QauntityForm(forms.ModelForm):
	class Meta:
		model = CartItem 
		fields = {'product','quantity'}