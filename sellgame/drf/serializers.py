from rest_framework import serializers

from news.models import News
from catalog.models import Product


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
