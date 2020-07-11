from rest_framework import serializers

from products.models import Product, Category

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id', 'name', 'description', 'price', 'category']


# Serializer para a categoria
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
