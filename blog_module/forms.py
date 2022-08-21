from django import forms
from .models import PostComment

class CommentForm(forms.ModelForm):
    model = PostComment
    field = '__all__'
    widgets = {
        'Name': forms.TextInput(attrs={}),
        'Comment': forms.Textarea(attrs={})
    }
