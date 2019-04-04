from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from users.models import User

class UserTests(APITestCase):
    test_data = {
        'username': 'testcreate',
        'email': 'testcreate@gmail.com',
        'password': 'createtest',
        
    }

    def test_create_account(self):
        url = reverse('users:user_signup')
        response = self.client.post(url, self.test_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # email hunter test
        data = self.test_data.copy()
        data['email'] = 'test@test.test'
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # clearbit test
        data = self.test_data.copy()
        data['username'] = 'testalex'
        data['email'] = 'alex@clearbit.com'
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.get(email=data['email']).first_name
        )

    def test_user_login(self):
        url = reverse('token_obtain_pair')

        # user creation before login test
        user = User.objects.create_user(**self.test_data)
        users_count = User.objects.count()
        self.assertGreaterEqual(users_count, 1)
        self.assertEqual(
            User.objects.get(username=user.username).username, 
            self.test_data['username']
        )

        # user login
        data = self.test_data.copy()
        del data['email']
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)