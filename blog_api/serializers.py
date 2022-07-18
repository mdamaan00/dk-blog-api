from dataclasses import fields
from rest_framework import serializers
from blog_api.models import *


class PostSerializer(serializers.ModelSerializer):
    post_author_username = serializers.ReadOnlyField(source="author.username")
    post_category = serializers.ReadOnlyField(source="category.title")
    class Meta:
        model = Post
        fields = ('id','image','title','author', 'post_author_username','post_category','excerpt','content','slug','status','published',)