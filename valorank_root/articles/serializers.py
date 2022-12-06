from rest_framework import serializers

from .models import Article, ArticleCategory

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('pk', 'title', 'category')


class ArticleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = ('pk', 'title')

class ArticleDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField('title', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'