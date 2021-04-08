from rest_framework import serializers
from apps.products.models import Product
from rest_framework.serializers import ValidationError


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'producer', 'characteristics']
