from rest_framework import serializers

from .models import Product, BaseRank, DesiredRank

class BaseRanksSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseRank
        fields = ('pk', 'title')


class DesiredRanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesiredRank
        fields = ('pk', 'title')


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('pk', 'title', 'current_price')


class ProductDetailSerializer(serializers.ModelSerializer):
    base_rank = serializers.SlugRelatedField(slug_field='title', read_only=True)
    desired_rank = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'