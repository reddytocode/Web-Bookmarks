from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.bookmarks.models import Bookmark
from apps.bookmarks.serializers import BookmarkSerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    """ Supports list, create, update and delete actions"""
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = []
    lookup_field = "id"
    lookup_url_kwarg = "bookmark_id"

    def get_permissions(self):
        if self.action != "list":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)