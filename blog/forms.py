from django import forms
from .models import Blog, Comment

# 만약 모델 기반이 아니라면 forms.Form
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title' , 'description']

# 댓글 모델
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']