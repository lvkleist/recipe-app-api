from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating user with email is scucesfl"""
        email = "davinciman7@gmail.com"
        password = "12345"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Email for new user normaliyed"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, '1234')
        self.assertEqual(email.lower(), user.email)

    def test_new_user_invalid_email(self):
        """Test cerating invalid emal"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_superuser(self):
        """Tests to create a superuser"""

        user = get_user_model().objects.create_superuser("hello@gmail.com", "test12")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)