from rest_framework import serializers
from apps.products.models import Product, Company
from rest_framework.serializers import ValidationError


class CompanyNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'description']
        
        
class ProductSerializer(serializers.ModelSerializer):
    producer = CompanyNestedSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'producer', 'characteristics']
        
    def update(self, instance, validated_data):
        print(validated_data)
        producer_data = validated_data.pop('producer')
        instance = super().update(instance, validated_data)
        producer = Company.objects.filter(pk=producer_data.get('id')).first()
        print(producer)
        if not producer:
            raise ValidationError('asdasd')
        instance.producer = producer
        instance.save()
        return instance
