from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0 # Draft
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='user_likes',
        blank=True
    )

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title