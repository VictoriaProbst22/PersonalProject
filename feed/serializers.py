from rest_framework import serializers
from .models import Post


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text']