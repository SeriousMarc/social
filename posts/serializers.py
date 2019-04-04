from rest_framework import serializers
from posts.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'status']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['likes']


class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['likes']


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'body', 'author', 'publish']


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Post
        fields = ['pk', 'title', 'body', 'author', 'publish', 'likes']