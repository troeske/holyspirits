from django.db import models
from cloudinary.models import CloudinaryField


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    hero_image = CloudinaryField('image', default='placeholder')

    class Meta:
        verbose_name_plural = 'Product Categories'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductType(models.Model):
    name = models.CharField(max_length=100, default='Whiskey')
    description = models.TextField(null=True, blank=True)
    hero_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    link_text = models.CharField(max_length=100, default='Visit Website')
    alt_text = models.CharField(max_length=100, default='logo')
    logo = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CaskType(models.Model):
    name = models.CharField(max_length=100, default='Wooden Cask')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Bottler(models.Model):
    name = models.CharField(max_length=100, default='Original Brand')
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    link_text = models.CharField(max_length=100, default='Visit Website', null=True, blank=True)
    alt_text = models.CharField(max_length=100, default='logo', null=True, blank=True)
    logo = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Product(models.Model):
    gtin = models.CharField(max_length=14, primary_key=True)  # Define gtin as CharField with max_length 14 and primary key
    name = models.CharField(max_length=250, default='whiskey')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_category')
    type = models.ForeignKey(ProductType, default="Whiskey", null=True, blank=True, on_delete=models.SET_NULL, related_name='product_type')
    region = models.CharField(max_length=250, default='', blank=True)
    brand = models.ForeignKey(ProductBrand, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_brand')
    bottler = models.ForeignKey(Bottler, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_bottler')
    cask_type = models.ForeignKey(CaskType, null=True, blank=True, on_delete=models.SET_NULL, related_name='cask_type')
    abv = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    vintage = models.IntegerField(null=True, blank=True)
    size = models.ForeignKey(ProductSize, null=True, blank=True, on_delete=models.SET_NULL, related_name='product_size')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    list_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["name", "type", "product_category"]

    def __str__(self):
        return f"{self.name} | {self.brand} | {self.gtin}" 


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = CloudinaryField('image', default='placeholder')
    alt_text = models.CharField(max_length=254, default='picture')

    def __str__(self):
        return self.product.name


class TasteCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    icon = CloudinaryField('image', default='placeholder')
    fa_icon = models.CharField(max_length=50, null=True, blank=True)
    alt_text = models.CharField(max_length=100, null=True, blank=True, default='icon')

    class Meta:
        verbose_name_plural = 'Taste Categories'
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProductTasteCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    taste_category = models.ForeignKey(TasteCategory, on_delete=models.CASCADE, related_name='taste_category')

    class Meta:
        verbose_name_plural = 'Product Taste Categories'
        unique_together = ('product', 'taste_category')

    def __str__(self):
        return f"{self.product.name} | {self.taste_category.name}"
