from django.urls import path, include

from apps.bookmarks.views import BookmarksViewSet

app_name = "bookmarks"

urlpatterns = [
    path('bookmarks/', BookmarksViewSet.as_view({"get": "list", "post": "create"}), name="bookmark-list"),
]
