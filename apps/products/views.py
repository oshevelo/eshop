from rest_framework import generics
from apps.products.models import Product
from django.shortcuts import get_object_or_404
from apps.products.serializers import ProductSerializer
#from apps.products.filters import MediaFilter
#from rest_framework.permissions import IsAuthenticatedOrReadOnly,BasePermission, SAFE_METHODS
#from rest_framework import filters


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #filter_class = MediaFilter


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))
