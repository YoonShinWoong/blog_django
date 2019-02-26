from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = RichTextUploadingField(blank=True,null=True)
    body = models.TextField()
    username = models.CharField(max_length=50)

    # title로 객체를 가르키기
    def __str__(self):
        return self.title

    # 내용 줄이기
    def summary(self):
        return self.body[:100]

# 댓글 모델
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments') # 관계 설정
    comment_date = models.DateTimeField(auto_now_add =True) # 댓글 날짜
    comment_body = models.CharField(max_length=200) # 댓글 내용
    comment_user = models.CharField(max_length=50)

    