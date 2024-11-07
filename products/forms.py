from django import forms
from .models import * 
from crispy_forms.helper import FormHelper
from cloudinary.forms import CloudinaryFileField


class ProductBrandForm(forms.ModelForm):
    remove_logo = forms.BooleanField(required=False, label='Remove Logo')
    
    class Meta:
        model = ProductBrand
        fields = '__all__'


class BottlerForm(forms.ModelForm):
    remove_logo = forms.BooleanField(required=False, label='Remove Logo')
    
    class Meta:
        model = Bottler
        fields = '__all__'
    

class CaskTypeForm(forms.ModelForm):
    class Meta:
        model = CaskType
        fields = ['name', 'description']


class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    remove_image = forms.BooleanField(required=False, label='Remove Thumbnail')
    
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        categories = ProductCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['product_category'].choices = friendly_names
        
        # Create form helper
        self.helper = FormHelper()
        self.helper.form_tag = False
        
        # Add styling class to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
        
        # Specifically adjust 'name' field
        self.fields['name'].widget.attrs['class'] += ' form-control'
        self.fields['name'].widget.attrs['style'] = 'width: 100%;'
        self.fields['description'].widget.attrs['class'] += ' form-control'
        self.fields['description'].widget.attrs['style'] = 'width: 100%;'


class ProductImageForm(forms.ModelForm):
    image = CloudinaryFileField(
        required=False  
    )
    
    class Meta:
        model = ProductImage
        exclude = ['product']


class ProductTasteCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductTasteCategory
        fields = ['taste_category'] 
        widgets = {
            'taste_category': forms.HiddenInput(),  # Hide the input field
        }


class TasteCategorySelectionForm(forms.Form):
    taste_categories = forms.ModelMultipleChoiceField(
        queryset=TasteCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
