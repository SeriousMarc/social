from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from posts.models import Post

class PostAPITest(APITestCase):
    def setUp(self):
        self.test_data = {
            'username': 'testcreate',
            'email': 'testcreate@gmail.com',
            'password': 'createtest',
        }
        self.client = APIClient()
        user = User.objects.create_user(**self.test_data)
        self.user = user

        self.post_data = {
            'title': 'test title',
            'slug': 'testslug',
            'body': 'test body',
            'status': 0,
            'author': user
        }
        post = Post.objects.create(**self.post_data)
        self.post = post

    def get_token(self):
        url = reverse('token_obtain_pair')
        data = self.test_data.copy()
        del data['email']
        response = self.client.post(url, data, format='json')
        token = response.data['access']
        return token

    def user_created(self):
        users_count = User.objects.count()
        self.assertGreaterEqual(users_count, 1)
        self.assertEqual(
            User.objects.get(username=self.user.username).username, 
            self.test_data['username']
        )


    def test_post_creation(self):
        token = self.get_token()

        # test creating
        url = reverse('posts:post_create')
        data = self.post_data.copy()
        data['slug'] = 'testslug1'
        del data['author']
        response = self.client.post(
            url, 
            data, 
            HTTP_AUTHORIZATION=f'Bearer {token}',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        p = Post.objects.get(slug=data['slug'])
        self.assertEqual(p.author, self.user)


    def test_post_unauthorized_creation(self):
        url = reverse('posts:post_create')
        data = self.post_data.copy()
        data['slug'] = 'testslug1'
        del data['author']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_post_like(self):
        url = reverse('posts:post_like', kwargs={'pk': self.post.pk})
        token = self.get_token()
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(self.post.likes.count(), 1)


    def test_post_like_unauthorized(self):
        url = reverse('posts:post_like', kwargs={'pk': self.post.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_dislike(self):
        url = reverse('posts:post_dislike', kwargs={'pk': self.post.pk})
        token = self.get_token()
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(self.post.likes.count(), 1)

    def test_post_dislike_unauthorized(self):
        url = reverse('posts:post_dislike', kwargs={'pk': self.post.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)