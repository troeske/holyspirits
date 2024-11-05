from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<gtin>', views.edit_product, name='edit_product'), 
    path('delete/<gtin>', views.delete_product, name='delete_product'), 
    path('add-related-brand/', views.add_related_brand, name='add_related_brand'),
    path('<gtin>/', views.product_details, name='product_details'),
    path('edit-related-brand/<int:pk>/', views.edit_related_brand, name='edit_related_brand'),
]
