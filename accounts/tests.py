from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SignupTests(TestCase):
    
    def test_signup(self):
        response_0 = self.client.get(reverse('sigup'))
        response_1 = self.client.get('/accounts/signup')
        self.assertEqual(response_0.status_code, 200)
        self.assertEqual(response_1.status_code, 200)
        self.assertTemplateUsed(response_1, 'registration/sigup.html')
    
    def test_login(self):
        response_2 = self.client.get(reverse('login'))
        response_3 = self.client.get('/accounts/login')
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_3.status_code, 200)
    
    def test_signup_form(self):
        username = "testuser"
        email = "testuser@gmail.com"
        get_user_model().objects.create_user(username, email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, username)
        self.assertEqual(get_user_model().objects.all()[0].email, email)
