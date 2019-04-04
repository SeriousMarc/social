from django.urls import path
from .views import (
    PostListAPIView, PostDetailAPIView, PostCreateAPIView,
    PostLikeView, PostDislikeView
)

app_name = 'posts'

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='post_create'),
    path('list/', PostListAPIView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('<int:pk>/dislike/', PostDislikeView.as_view(), name='post_dislike'),
]