from django import forms
from .models import PostComment
from django.core import validators

class CommentForm(forms.Form):
    text = forms.CharField(
        label='Add your comment',
        widget=forms.Textarea(attrs={'class': 'comment_input', 'id': 'commentText', 'placeholder': 'Add your comment'})
    )
