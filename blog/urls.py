from django.urls import path

from blog.views import (PostCreateView, PostDeleteView, PostDetailView,
                        PostListView, PostUpdateView)

app_name = "blog"


urlpatterns = [
    path("", PostListView.as_view(), name="blog"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
