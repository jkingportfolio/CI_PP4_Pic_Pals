# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
# Internal
from .models import Post, Like
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestPostModels(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and test user profile
         """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com'
        )
        test_post = Post.objects.create(
            id='1',
            created_date=datetime.now(),
            user=test_user,
            caption='test caption',
            likes='0'
        )
        test_like = Like.objects.create(post=test_post, user=test_user)



    def tearDown(self):
        """
        Delete test user and test post
        """
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_like_str_method(self):
        """
        This test tests the post likes
        """
        test_post = Post.objects.get(user='test_user')
        test_like = Like.objects.get(user='test_user')
        self.assertEqual(str(test_like), f'{self.user} liked {self.post}')