import rest_framework 
from .models import Post

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text']