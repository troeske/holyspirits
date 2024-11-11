from django import forms
from django.forms import inlineformset_factory
from .models import * 
from crispy_forms.helper import FormHelper
from cloudinary.forms import CloudinaryFileField
from django.forms.models import BaseInlineFormSet


class ProductBrandForm(forms.ModelForm):
    """
    Form to handle edit and add a Brand
    """
    remove_logo = forms.BooleanField(required=False, label='Remove Logo')

    class Meta:
        model = ProductBrand
        fields = '__all__'


class BottlerForm(forms.ModelForm):
    """
    Form to handle edit and add a Bottler
    """
    remove_logo = forms.BooleanField(required=False, label='Remove Logo')

    class Meta:
        model = Bottler
        fields = '__all__'


class CaskTypeForm(forms.ModelForm):
    """
    Form for future handling edit and add a CaskType
    """
    class Meta:
        model = CaskType
        fields = ['name', 'description']


class ProductSizeForm(forms.ModelForm):
    """
    Form for future handling edit and add a Size
    """
    class Meta:
        model = ProductSize
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    """
    ProductForm is a Django ModelForm for the Product model. It includes a custom
    BooleanField 'remove_image' to handle the removal of product thumbnails.
    Attributes:
        remove_image (forms.BooleanField): A field to indicate whether the product
            thumbnail should be removed.
    Meta:
        model (Product): The model that this form is associated with.
        fields (str): Specifies that all fields from the Product model should be
            included in the form.
        widgets (dict): Custom widgets for the 'brand' and 'bottler' fields to
            apply specific HTML attributes.
    Methods:
        __init__(self, *args, **kwargs): Initializes the form, sets choices for
            'product_category' field, creates a form helper, and adds styling
            classes to all fields.
    """
    remove_image = forms.BooleanField(required=False, label='Remove Thumbnail')

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'brand': forms.Select(attrs={'id': 'brand_select', 'class': 'form-control'}),
            'bottler': forms.Select(attrs={'id': 'bottler_select', 'class': 'form-control'}),
        }

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
            field.widget.attrs['class'] = 'border-black rounded'

        # Specifically adjust 'name' field
        self.fields['name'].widget.attrs['class'] += ' form-control'
        self.fields['name'].widget.attrs['style'] = 'width: 100%;'
        self.fields['description'].widget.attrs['class'] += ' form-control'
        self.fields['description'].widget.attrs['style'] = 'width: 100%;'


class ProductImageForm(forms.ModelForm):
    """
    Form to handle edit and add a Product Images
    """
    image = CloudinaryFileField(
        required=False
    )

    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']


class TasteCategorySelectionForm(forms.Form):
    """
    Form to handle adding of Taste Categories
    """
    taste_categories = forms.ModelMultipleChoiceField(
        queryset=TasteCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class ProductTasteCategoryForm(forms.ModelForm):
    """
    Form to handle display and delete of ProductTasteCategory instances.
    """
    class Meta:
        model = ProductTasteCategory
        fields = ['taste_category'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Render taste_category as a hidden field
        self.fields['taste_category'].widget = forms.HiddenInput()

    def validate_unique(self):
        """
        Override the default validate_unique to prevent unique constraint
        validation errors during form validation.
        """
        pass  


class IgnoreDuplicatesProductTasteCategoryFormSet(BaseInlineFormSet):
    """
    A custom formset basic structure suggested by ChatGPT, that ensures no duplicate
    taste categories are added to a product.
    This formset performs the following tasks:
    - Cleans the formset to check for duplicate taste categories.
    - Saves the formset while handling deletions first to avoid uniqueness constraint violations.
    - Deletes instances marked for deletion and returns a list of remaining instances.
    Methods:
    - clean(): Validates the formset to ensure no duplicate taste categories are present.
    - save(commit=True): Saves the formset, processing deletions before saves to maintain uniqueness.
    - delete_existing(): Deletes instances marked for deletion and returns a list of remaining instances.
    """
    def clean(self):
        super().clean()
        if any(self.errors):
            return

        # Track taste_category_ids to detect duplicates in the formset
        taste_category_ids = set()
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue  # Skip forms marked for deletion
            if not form.cleaned_data:
                continue  # Skip empty forms
            taste_category = form.cleaned_data.get('taste_category')
            if taste_category:
                if taste_category.id in taste_category_ids:
                    form.add_error('taste_category', 'Duplicate taste category in the formset.')
                else:
                    taste_category_ids.add(taste_category.id)

    def save(self, commit=True):
        """
        Save method that processes deletions before saves.
        This ensures that uniqueness constraints are not violated.
        """
        # Delete instances first
        instances = self.delete_existing()

        # Then save or create instances
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue  # Already deleted
            if not form.cleaned_data:
                continue  # Skip empty forms

            taste_category = form.cleaned_data.get('taste_category')
            if taste_category:
                # Use get_or_create to prevent duplicates
                association, created = ProductTasteCategory.objects.get_or_create(
                    product=self.instance,
                    taste_category=taste_category
                )
                instances.append(association)

        if commit:
            for instance in instances:
                instance.save()

        return instances

    def delete_existing(self):
        """
        Deletes instances marked for deletion and returns a list of remaining instances.
        """
        instances = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                instance = form.instance
                if instance.pk:
                    instance.delete()
                continue
            else:
                instance = form.instance
                if instance.pk:
                    instances.append(instance)
        return instances


# Define the ProductImageFormSet here
ProductImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    form=ProductImageForm,
    extra=1,  # You can adjust 'extra' as needed
    can_delete=True
)

# Create a custom inline formset for ProductTasteCategory with the custom formset class
ProductTasteCategoryFormSet = inlineformset_factory(
        Product,
        ProductTasteCategory,
        form=ProductTasteCategoryForm,
        formset=IgnoreDuplicatesProductTasteCategoryFormSet,
        extra=0,
        can_delete=True
    )
