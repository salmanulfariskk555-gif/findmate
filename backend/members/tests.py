from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Profile, Block

class RegistrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_under_18_is_rejected(self):
        today = date.today()
        underage = today.replace(year=today.year - 17)
        response = self.client.post("/api/auth/register/", {
            "username": "younguser",
            "password": "A-long-test-password-92!",
            "display_name": "Young User",
            "birth_date": underage.isoformat(),
        }, format="json")
        self.assertEqual(response.status_code, 400)

    def test_adult_registration_creates_hidden_profile(self):
        adult = date.today().replace(year=date.today().year - 25)
        response = self.client.post("/api/auth/register/", {
            "username": "adultuser",
            "password": "A-long-test-password-92!",
            "display_name": "Adult User",
            "birth_date": adult.isoformat(),
        }, format="json")
        self.assertEqual(response.status_code, 201)
        profile = Profile.objects.get(user__username="adultuser")
        self.assertFalse(profile.visible)
        self.assertFalse(profile.approved)

class SafetyEndpointTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="one", password="test-pass-123456")
        self.other = User.objects.create_user(username="two", password="test-pass-123456")
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_user_can_block_another_user(self):
        response = self.client.post(f"/api/block/{self.other.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Block.objects.filter(blocker=self.user, blocked=self.other).exists())

    def test_user_cannot_block_self(self):
        response = self.client.post(f"/api/block/{self.user.pk}/")
        self.assertEqual(response.status_code, 400)

    def test_account_deletion_requires_password(self):
        response = self.client.delete("/api/account/delete/", {"password": "wrong"}, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertTrue(User.objects.filter(pk=self.user.pk).exists())

    def test_account_deletion_removes_user_and_profile(self):
        Profile.objects.create(user=self.user, display_name="One", birth_date=date(1995, 1, 1))
        response = self.client.delete("/api/account/delete/", {"password": "test-pass-123456"}, format="json")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
        self.assertFalse(Profile.objects.filter(user_id=self.user.pk).exists())
