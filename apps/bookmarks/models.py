from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Bookmark(models.Model):
    is_private = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name="bookmarks", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())

