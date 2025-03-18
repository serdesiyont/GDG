from django.db import models
from django.core.validators import MinLengthValidator

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField(validators=[MinLengthValidator(100)])  # Content of the blog post with a minimum length validator
    name = models.CharField(max_length=100)  # Name of the author
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the blog post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the blog post was last updated

    def __str__(self):
        return self.title  # String representation of the blog post

class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)  # Foreign key to the blog post
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was created

    def __str__(self):
        return f'Comment by on {self.blogpost}'  # String representation of the comment
