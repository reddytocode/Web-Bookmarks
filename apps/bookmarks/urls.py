from django.urls import path, include

from apps.bookmarks.views import BookmarksViewSet

app_name = "bookmarks"

urlpatterns = [
    path('/', BookmarksViewSet.as_view({"get": "list", "post": "create"}), name="bookmark-list"),
    path('/<bookmark_id>', BookmarksViewSet.as_view({"patch": "partial_update", "delete": "destroy"}), name="bookmark-update"),
]
