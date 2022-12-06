from rest_framework import serializers

from store.models import Product
from articles.models import Article

class MainPageProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('pk', 'title', 'price')


class MainPageArticlesSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'title', 'category')