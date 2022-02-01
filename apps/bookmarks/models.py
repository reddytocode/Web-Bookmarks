from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    is_private = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name="bookmarks", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    # https://www.geeksforgeeks.org/maximum-length-of-a-url-in-different-browsers/#:~:text=Google%20Chrome%20allows%20the%20maximum,size%202MB(2048%20characters).&text=In%20Firefox%20the%20length%20of,no%20longer%20displays%20the%20URL.
    url = models.CharField(max_length=2048)
    created_at = models.DateTimeField()
