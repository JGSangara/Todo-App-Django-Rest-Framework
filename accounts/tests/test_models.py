from django.test import TestCase
from accounts.models import User


class TestUserModel(TestCase):

    def setUp(self):
        self.email = 'test@example.com'
        self.password = 'password123'

    def test_create_user(self):
        user = User.objects.create_user(email=self.email, password=self.password)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_create_superuser(self):
        user = User.objects.create_superuser(email=self.email, password=self.password)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password=self.password)

    def test_str(self):
        user = User.objects.create_user(email=self.email, password=self.password)
        self.assertEqual(str(user), self.email)

    def test_has_perm(self):
        user = User.objects.create_user(email=self.email, password=self.password)
        self.assertTrue(user.has_perm('accounts.view_user'))

    def test_has_module_perms(self):
        user = User.objects.create_user(email=self.email, password=self.password)
        self.assertTrue(user.has_module_perms('accounts'))
