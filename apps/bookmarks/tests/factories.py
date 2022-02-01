import factory
from django.contrib.auth.models import User
from django.utils import timezone

from apps.bookmarks.models import Bookmark


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"test-user-{n}")
    password = factory.PostGenerationMethodCall("set_password", "1234")


class BookmarkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bookmark

    is_private = False
    created_by = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: f"fake-title-{n}")
    url = factory.Sequence(lambda n: f"fake-url-{n}")
    created_at = timezone.now()
