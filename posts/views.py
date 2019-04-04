from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from posts import serializers
from .models import Post


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostLikeSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('post',)
    

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.likes.add(self.request.user)
        return self.update(request, *args, **kwargs)


class PostDislikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDislikeSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('post',)


    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.likes.remove(self.request.user)
        return self.update(request, *args, **kwargs)


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer
    permission_classes = (AllowAny,)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    permission_classes = (AllowAny,)