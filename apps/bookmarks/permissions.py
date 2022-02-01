from rest_framework.permissions import BasePermission

from apps.bookmarks.models import Bookmark


class BookmarkEditPermissions(BasePermission):
    def has_permission(self, request, view):
        obj = Bookmark.objects.filter(id=view.kwargs.get("bookmark_id")).first()
        return obj.created_by == request.user
