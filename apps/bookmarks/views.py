from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.bookmarks.models import Bookmark
from apps.bookmarks.serializers import BookmarkSerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    """ Supports list, create, update and delete actions"""
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    lookup_url_kwarg = "bookmark_id"


