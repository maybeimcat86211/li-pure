from django.db import models
from django.utils import timezone
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)  #位置名稱
    def __str__(self):
        return self.name #顯示地點位置

class Post(models.Model):
    subject = models.CharField(max_length=255)  #標題
    content = models.CharField(max_length=255)  #內容
    author = models.CharField(max_length=20)  #貼文者
    publish_date = models.DateField(default=timezone.now)  #貼文時間
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #位置，CASCADE連帶刪除