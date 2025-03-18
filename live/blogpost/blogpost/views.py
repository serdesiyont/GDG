from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

def blogpost_list(request):
    try:
        posts = BlogPost.objects.all()  # Retrieve all blog posts
    except BlogPost.DoesNotExist:
        posts = []  # Handle case where no blog posts exist
    return render(request, 'blogpost_list.html', {'posts': posts})  # Render the blog post list template

def blogpost_detail(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)  # Retrieve the blog post by primary key
        comments = post.comments.all()  # Retrieve all comments for the blog post
    except BlogPost.DoesNotExist:
        post = None
        comments = []  # Handle case where the blog post does not exist
    if request.method == "POST":
        comment_form = CommentForm(request.POST)  # Create a comment form instance with POST data
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blogpost = post  # Associate the comment with the blog post
            comment.save()  # Save the comment
            return redirect('blogpost_detail', pk=post.pk)  # Redirect to the blog post detail page
    else:
        comment_form = CommentForm()  # Create an empty comment form instance
    return render(request, 'blogpost_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})  # Render the blog post detail template

def blogpost_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)  # Create a blog post form instance with POST data
        if form.is_valid():
            form.save()  # Save the blog post
            return redirect('blogpost_list')  # Redirect to the blog post list page
    else:
        form = BlogPostForm()  # Create an empty blog post form instance
    return render(request, 'blogpost_form.html', {'form': form})  # Render the blog post form template

def blogpost_update(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)  # Retrieve the blog post by primary key
    except BlogPost.DoesNotExist:
        post = None  # Handle case where the blog post does not exist
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)  # Create a blog post form instance with POST data and the existing post
        if form.is_valid():
            form.save()  # Save the updated blog post
            return redirect('blogpost_detail', pk=post.pk)  # Redirect to the blog post detail page
    else:
        form = BlogPostForm(instance=post)  # Create a blog post form instance with the existing post
    return render(request, 'blogpost_form.html', {'form': form})  # Render the blog post form template

def blogpost_delete(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)  # Retrieve the blog post by primary key
    except BlogPost.DoesNotExist:
        post = None  # Handle case where the blog post does not exist
    if request.method == "POST" and post:
        post.delete()  # Delete the blog post
        return redirect('blogpost_list')  # Redirect to the blog post list page
    return render(request, 'blogpost_confirm_delete.html', {'post': post})  # Render the blog post delete confirmation template
