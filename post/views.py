from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.serializers import PostSerializer
from post.models import Post
# Create your views here.


class PostListView(ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer