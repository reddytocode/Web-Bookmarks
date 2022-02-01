from rest_framework import serializers

from apps.bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ("is_private", "title", "url", "created_at")
        read_only_fields = ("created_at",)