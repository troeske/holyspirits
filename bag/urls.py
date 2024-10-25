from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_gtin>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_gtin>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_gtin>/', views.remove_from_bag, name='remove_from_bag'),
]
