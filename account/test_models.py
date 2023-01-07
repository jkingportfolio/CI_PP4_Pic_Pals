"""
A module for testing views of the account app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
# Internal
from .models import Profile, Follow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProfileModels(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and test user profile
         """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        testuser.save()

    def tearDown(self):
        """
        Delete test user and Profile
        """
        User.objects.all().delete()

    def test_profile_str_method(self):
        """
        This test tests the users profile username
        """
        testuser = User.objects.get(username='test_user')
        profile = Profile.objects.create(user=testuser)
        self.assertEqual(str(profile), f'Profile of {profile.user.username}')


class TestFollowModels(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         and followed_account user
         """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password')
        # test_user_profile = Profile.objects.create(user=test_user)
        test_user.save()
        # test_user_profile.save()

        test_followed_account = User.objects.create_user(
            username='test_followed_account',
            password='test_password')
        # test_followed_account_profile = Profile.objects.create(user=test_followed_account) 
        test_followed_account.save()
        # test_followed_account_profile.save()

        test_follow = Follow.objects.create(
            user=test_user, followed_account=test_followed_account)
        test_follow.save()

    def tearDown(self):
        """
        Delete test user and Follow object
        """
        User.objects.all().delete()
        # Profile.objects.all().delete()
        Follow.objects.all().delete()

    def test_follow_str_method(self):
        """
        This test tests the follow object between user and followed_account
        """
        test_follow = Follow.objects.get(
            user=test_user, followed_account=test_followed_account)
        self.assertEqual((test_follow.__str__()),
                         f'{self.user} followed {self.followed_account}')
