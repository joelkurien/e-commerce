from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_page, name='product' ),
    path('addproducts/', views.product_add, name='addproduct')
]
