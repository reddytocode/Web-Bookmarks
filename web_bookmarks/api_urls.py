from django.urls import path, include

urlpatterns = [
    path('bookmarks/', include("apps.bookmarks.urls")),
]
