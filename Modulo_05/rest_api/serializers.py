from rest_framework import serializers

from products.models import Product, Category, Order

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id', 'name', 'description', 'price', 'category']


# Serializer para a categoria
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


# Serializer para Orders
class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'payment', 'products', 'total_amount']