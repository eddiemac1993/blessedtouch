from django.urls import path, include
from . import views

app_name = 'ecommerce'

urlpatterns = [

    path('', views.coming_soon, name='coming_soon'),
    path('product/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.product_add, name='product_add'),
    path('<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]
