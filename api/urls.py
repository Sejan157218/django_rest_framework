from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverviews,name='api-overview'),
    path('products/',views.Products,name='all-products'),
    path('products/<str:pk>/',views.SingleProducts,name='single-products'),
    path('product-create/',views.CreateProduct,name='create-product'),
    path('product-update/<str:pk>',views.ProductUpdate,name='create-update'),
    path('product-delete/<str:pk>',views.ProductDelete,name='create-delete')
]
