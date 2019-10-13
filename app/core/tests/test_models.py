from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test create a new user with email is successful"""
        email = 'test@depaulian.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test for a new user email is normalized"""
        email = 'test@DEPAULIAN.COM'
        user = get_user_model().objects.create_user(email, '123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@depaulian.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
