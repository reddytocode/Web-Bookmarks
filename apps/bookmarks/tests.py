from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class BookmarkBaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test_user", None, "1234")
        self.app = APIClient()
        self.login(self.user)

    def login(self, user, password="1234"):
        pass

    def logout(self):
        pass


class BookmarkListTests(BookmarkBaseTest):
    def setUp(self):
        super().setUp()
        self.url = reverse("bookmarks:bookmark-list")
        self.login(self.user)

    def test_access(self):
        # logged in user and not logged in users have access
        response = self.app.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.logout(self.user)
        response = self.app.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_logged_user(self):
        pass

    def test_list_anonymous_user(self):
        pass

