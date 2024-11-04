from django import forms
from .models import Product, ProductCategory, ProductBrand, CaskType


class ProductBrandForm(forms.ModelForm):
    remove_logo = forms.BooleanField(required=False, label='Remove Logo')
    
    class Meta:
        model = ProductBrand
        fields = '__all__'
    
    

class CaskTypeForm(forms.ModelForm):
    class Meta:
        model = CaskType
        fields = ['name', 'description']



class ProductForm(forms.ModelForm):
    remove_image = forms.BooleanField(required=False, label='Remove Image')
    
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ProductCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['product_category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'