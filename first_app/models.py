from django.db import models

# Create your models here.

class Comment(models.Model):
    user=models.CharField(max_length=50)
    comment=models.TextField()
    def __str__(self):
        return self.user+" : "+self.comment

