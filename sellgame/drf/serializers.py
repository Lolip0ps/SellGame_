from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.Serializer):
    class Meta:
        model = News
        fields = ('title', 'content')
