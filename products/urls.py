from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<gtin>/', views.product_details, name='product_details'), # needs to be tested
]
