from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_page, name='product' ),
    path('addproducts/', views.product_add, name='addproduct'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('<int:id>/products/', views.user_page, name='userpage')
]
