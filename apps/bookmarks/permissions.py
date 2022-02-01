from rest_framework.permissions import BasePermission

from apps.bookmarks.models import Bookmark


class BookmarkEditPermissions(BasePermission):
    # def has_permission(self, request, view):
    #     obj = view.get_object()
    #     import pdb
    #     pdb.set_trace()
    #     return False

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
