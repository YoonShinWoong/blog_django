from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    username = models.CharField(max_length=50)

    # title로 객체를 가르키기
    def __str__(self):
        return self.title

    # 내용 줄이기
    def summary(self):
        return self.body[:100]