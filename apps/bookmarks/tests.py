from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class BookmarkBaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test_user", None, "1234")
        self.app = APIClient()
        self.url = reverse("bookmarks:bookmark-list")
        self.login(self.user)

    def login(self, user, password="1234"):
        self.app.login(username=user.username, password=password)


class BookmarkListTests(BookmarkBaseTest):
    def setUp(self):
        super().setUp()

    def test_access(self):
        # logged in user and not logged in users have access
        self.login(self.user)
        response = self.app.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.app.logout()
        response = self.app.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_logged_user(self):
        pass

    def test_list_anonymous_user(self):
        pass


class BookmarkCreateTests(BookmarkBaseTest):
    def setUp(self):
        super().setUp()
        self.data = {
            "is_private": False,
            "title": "fake-bookmark",
            "url": "fake-url",
        }

    def test_access(self):
        # Just authenticated user has access
        self.login(self.user)
        response = self.app.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.app.logout()
        response = self.app.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
