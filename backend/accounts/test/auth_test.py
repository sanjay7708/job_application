from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
class TestLogin(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='sanjay',email='sanjay@gmail.com',password='7708')
        self.login_url=reverse('login')
        self.signup_url=reverse('signup')
        self.logout_url=reverse('logout')

    def test_login_success(self):
        data={
            'username':'sanjay',
            'password':'7708'

        }

        res=self.client.post(self.login_url,data)
        self.assertEqual(res.data['message'],'login successfully')
        self.assertEqual(res.status_code,status.HTTP_200_OK)
    
    def test_login_fail(self):
        data={
            'username':'sanjay',
            'password':'770'

        }
        res=self.client.post(self.login_url,data)
        self.assertEqual(res.data['message'],'invalid credentials')
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_signup_success(self):
        data={
            'username':'maha',
            'email':'maha@gami.com',
            'password':'7708',
            'confirm_password':'7708'
        }
        res=self.client.post(self.signup_url,data)
        self.assertEqual(res.data['message'],'User Register Successfully')
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username=data['username']).exists())

    def test_signup_failed(self):
        data={
            'username':'maha',
            'email':'sanjay@gmail.com',
            'password':'7708',
            'confirm_password':'7708'
        }

        res=self.client.post(self.signup_url,data,format='json')
        
        self.assertEqual(res.data['non_field_errors'][0],'email already registered')
    
        
    def test_logout_success(self):
        refresh_token=RefreshToken.for_user(self.user)
        
        data={
            'refresh':str(refresh_token)
        }
        res=self.client.post(self.logout_url,data,format='json')
        self.assertEqual(res.status_code,status.HTTP_205_RESET_CONTENT)



    def test_logout_failed(self):
        res=self.client.post(self.logout_url)
        
        self.assertEqual(res.data['message'],"refresh token must require")
        self.assertEqual(res.status_code,status.HTTP_200_OK)