from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<gtin>', views.edit_product, name='edit_product'), 
    path('delete/<gtin>', views.delete_product, name='delete_product'), 
    path('add-related-model/<str:model_type>/', views.add_related_model, name='add_related_model'),
    path('edit-related-model/<str:model_type>/<int:pk>/', views.edit_related_model, name='edit_related_model'),
    path('add-taste-categories/<gtin>', views.add_taste_categories, name='add_taste_categories'),
    path('<gtin>/', views.product_details, name='product_details'),
]
