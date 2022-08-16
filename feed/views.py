from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from feed.apps import FeedConfig
from .serializers import FeedSerializer
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = FeedSerializer(posts, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FeedSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = FeedSerializer(posts);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FeedSerializer(posts, data= request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)