from .models import Product, Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(required=False)

    class Meta:
        model = Product
        fields = ('image', 'title', 'category', 'description', 'price', 'raiting')

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)
        product = Product.objects.create(**validated_data)

        if image_data:
            Image.objects.create(product=product, **image_data)

        return product


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
