
from turtle import pos
from unicodedata import category
from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog_api.models import *
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def allBlog(request):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer(queryset,many=True)
    return Response(serializer_class.data)

@api_view(['GET'])
def singleBlog(request,pk=None):
    post = Post.postobjects.filter(slug=pk)
    serializer_class = PostSerializer(post,many=True)
    return Response(serializer_class.data)


'''class PostList(viewsets.ModelViewSet):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
   
    

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, slug=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)

    def get_queryset(self):
        category = self.request.query_params.get('category',None)
        post = Post.objects.all()
        if category:
            post = Post.objects.filter(category=category)
        return post '''

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer