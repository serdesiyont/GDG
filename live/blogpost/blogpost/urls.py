from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogpost_list, name="blogpost_list"),  # URL for listing blog posts
    path("post/<int:pk>/", views.blogpost_detail, name="blogpost_detail"),  # URL for blog post detail
    path("post/new/", views.blogpost_create, name="blogpost_create"),  # URL for creating a new blog post
    path("post/<int:pk>/edit/", views.blogpost_update, name="blogpost_update"),  # URL for editing a blog post
    path("post/<int:pk>/delete/", views.blogpost_delete, name="blogpost_delete"),  # URL for deleting a blog post
]