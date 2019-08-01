from django.db import models

# Create your models here.

class Comment(models.Model):
    user=models.CharField(max_length=50)
    comment=models.TextField()
    def __str__(self):
        return self.user+" : "+self.comment


class Music(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    track_no=models.IntegerField(null=True)

    def __str__(self):
        return self.title
