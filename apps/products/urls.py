from django.urls import path, include
from apps.products import views


urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('<int:product_id>/', views.ProductDetails.as_view(), name='details')
    
]
