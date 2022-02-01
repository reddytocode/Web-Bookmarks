from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.bookmarks.models import Bookmark
from apps.bookmarks.permissions import BookmarkEditPermissions
from apps.bookmarks.serializers import BookmarkSerializer


class BookmarksViewSet(viewsets.ModelViewSet):
    """ Supports list, create, update and delete actions"""
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = []
    lookup_field = "id"
    lookup_url_kwarg = "bookmark_id"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by("-created_at")

    def get_permissions(self):
        print(self.action)
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        elif self.action in ("partial_update", "destroy"):
            self.permission_classes = [IsAuthenticated, BookmarkEditPermissions]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, created_at=timezone.now())