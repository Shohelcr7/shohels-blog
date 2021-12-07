from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    category=models.CharField(max_length=20)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs= {'pk':self.pk})


