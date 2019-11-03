from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Type your comment',
        'id': 'username',
        'rows': '3'
    }))

    class Meta:
        model = Comment
        fields = ['author', 'content', ]
