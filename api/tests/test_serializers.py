from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from rest_framework.test import APITestCase

from accounts.models import User
from api.serializers import (PasswordResetConfirmSerializer,
                             PasswordResetSerializer, RegisterSerializer)


class RegisterSerializerTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'password2': 'password123'
        }

    def test_serializer_with_valid_data(self):
        serializer = RegisterSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_passwords_not_matching(self):
        self.data['password2'] = 'password456'
        serializer = RegisterSerializer(data=self.data)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_create_user(self):
        serializer = RegisterSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.data['email'])
        self.assertEqual(user.first_name, self.data['first_name'])
        self.assertEqual(user.last_name, self.data['last_name'])


class PasswordResetSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password='testpass',
            email='testuser@example.com',
            first_name='Test',
            last_name='User'
        )
        self.data = {'email': self.user.email}

    def test_serializer_with_valid_data(self):
        serializer = PasswordResetSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_email(self):
        self.data['email'] = 'invalid@example.com'
        serializer = PasswordResetSerializer(data=self.data)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_validate_email(self):
        serializer = PasswordResetSerializer(data=self.data)
        email = serializer.validate_email(self.user.email)
        self.assertEqual(email, self.user.email)

    def test_validate(self):
        serializer = PasswordResetSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        self.assertEqual(validated_data, self.data)


class PasswordResetConfirmSerializerTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password='testpass',
            email='testuser@example.com',
            first_name='Test',
            last_name='User'
        )
        self.token = default_token_generator.make_token(self.user)
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.data = {
            'new_password': 'newpass123',
            're_new_password': 'newpass123',
            'uidb64': self.uidb64,
            'token': self.token
        }

    def test_serializer_with_valid_data(self):
        serializer = PasswordResetConfirmSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        self.data['new_password'] = 'newpass123'
        self.data['re_new_password'] = 'invalidpass'
        serializer = PasswordResetConfirmSerializer(data=self.data)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_validate(self):
        serializer = PasswordResetConfirmSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        self.assertEqual(validated_data['new_password'], self.data['new_password'])
        self.assertEqual(validated_data['re_new_password'], self.data['re_new_password'])
        self.assertEqual(validated_data['uidb64'], self.data['uidb64'])
        self.assertEqual(validated_data['token'], self.data['token'])
