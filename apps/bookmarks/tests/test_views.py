from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from apps.bookmarks.models import Bookmark
from apps.bookmarks.tests.factories import UserFactory, BookmarkFactory


class BookmarkBaseTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
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

    def test_create(self):
        count = Bookmark.objects.count()
        fake_created_at = timezone.now()
        with freeze_time(fake_created_at):
            response = self.app.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bookmark.objects.count(), count+1)
        self.assertTrue(Bookmark.objects.filter(**self.data, created_by=self.user, created_at=fake_created_at).exists())


class BookmarkUpdateTests(BookmarkBaseTest):
    def setUp(self):
        super().setUp()
        self.bookmark = BookmarkFactory(created_by=self.user)
        self.url = reverse("bookmarks:bookmark-update", kwargs={"bookmark_id": self.bookmark.id})
        self.data = {
            "is_private": False,
            "title": "new-fake-bookmark",
            "url": "new-fake-url",
        }

    def test_access(self):
        # Just authenticated user has access
        self.login(self.user)
        response = self.app.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.app.logout()
        response = self.app.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        other_user = UserFactory()
        self.login(other_user)
        response = self.app.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update(self):
        count = Bookmark.objects.count()
        response = self.app.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Bookmark.objects.count(), count)
        self.assertTrue(Bookmark.objects.filter(**self.data, created_by=self.user).exists())


class BookmarkDeleteTests(BookmarkBaseTest):
    def setUp(self):
        super().setUp()
        self.bookmark = BookmarkFactory(created_by=self.user)
        self.url = reverse("bookmarks:bookmark-update", kwargs={"bookmark_id": self.bookmark.id})

    def test_access(self):
        self.app.logout()
        response = self.app.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        other_user = UserFactory()
        self.login(other_user)
        response = self.app.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.login(self.user)
        response = self.app.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete(self):
        count = Bookmark.objects.count()
        self.assertTrue(Bookmark.objects.filter(id=self.bookmark.id).exists())
        response = self.app.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bookmark.objects.count(), count-1)
        self.assertFalse(Bookmark.objects.filter(id=self.bookmark.id).exists())
