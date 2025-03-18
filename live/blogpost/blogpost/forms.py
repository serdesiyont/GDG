from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'name']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long')  # Added validation for title
        return title

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long')  # Added validation for name
        return name

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 100:
            raise forms.ValidationError('Content must be at least 100 characters long')  # Added validation for content
        return content

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
