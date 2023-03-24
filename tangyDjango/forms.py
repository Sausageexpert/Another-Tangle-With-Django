from django import forms 
from .models import foodItems

class ItemForm(forms.ModelForm):
    class Meta:
        model=foodItems
        fields=['item_name','item_desc','item_price','item_image']

    
