from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'gtin',
        'name',
        'product_category',
        'price',
        'rating',
        'region',
    )

    ordering = ('name',)
    
admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(ProductBrand)
admin.site.register(ProductSize)
admin.site.register(CaskType)
admin.site.register(Bottler)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(ProductTastingNote)
admin.site.register(TasteCategory)
admin.site.register(ProductTasteCategory)