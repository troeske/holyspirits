from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<gtin>', views.product_details, name='product_details'),
]
