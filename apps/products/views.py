from rest_framework import generics

from django.shortcuts import get_object_or_404

from apps.products.serializers import ProductSerializer
from apps.products.models import Product, Company
#from apps.products.filters import MediaFilter
#from rest_framework.permissions import IsAuthenticatedOrReadOnly,BasePermission, SAFE_METHODS
#from rest_framework import filters


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))

